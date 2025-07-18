import pytest

from bedrock_switchboard.client import Bedrock


@pytest.mark.asyncio
async def test_basic_control_plane():
    client = Bedrock(region="us-east-2")

    models = await client.get_model_list()
    assert models is not None
    assert len(models) > 0

    model_details = await client.get_model_details(models[0]["modelId"])
    assert model_details is not None
    assert model_details["modelId"] == models[0]["modelId"]


@pytest.mark.asyncio
async def test_basic_runtime():
    client = Bedrock(region="us-east-2")

    completion = await client.get_completion(
        model_id="us.meta.llama3-1-8b-instruct-v1:0",
        prompt="What is the capital of France?",
    )
    assert completion is not None
    assert "Paris" in completion
