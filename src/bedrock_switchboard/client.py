import json
from typing import cast

import aioboto3
from types_aiobotocore_bedrock.client import BedrockClient
from types_aiobotocore_bedrock_runtime.client import BedrockRuntimeClient


class Bedrock:
    def __init__(self, region: str):
        self.region = region
        self.session = aioboto3.Session()

    def _bedrock(self):
        return self.session.client("bedrock", region_name=self.region)

    def _runtime(self):
        return self.session.client("bedrock-runtime", region_name=self.region)

    async def get_model_list(self):
        async with cast(BedrockClient, self._bedrock()) as client:
            response = await client.list_foundation_models()
        return response["modelSummaries"]

    async def get_model_details(self, model_id: str):
        async with cast(BedrockClient, self._bedrock()) as client:
            response = await client.get_foundation_model(modelIdentifier=model_id)
        return response["modelDetails"]

    async def get_completion(self, model_id: str, prompt: str) -> str:
        async with cast(BedrockRuntimeClient, self._runtime()) as client:
            response = await client.invoke_model(
                modelId=model_id,
                body=json.dumps({"prompt": prompt}),
                contentType="application/json",
            )
        body = await response["body"].read()
        return json.loads(body)["generation"]
