from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_feature_metadata():
    data=client.post("/v1/run",json={"value":"customer features"}).json()
    assert data["lineage_available"] is True
    assert data["features"][0]["freshness_min"] < data["stale_threshold_min"]
