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
