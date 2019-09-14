import json
import pytest
from src.movie_service import app


class TestMoviesByYear:
    @pytest.fixture
    def client(self):
        app.config["TESTING"] = True
        yield app.test_client()

    def test_get(self, client):
        year = 2000
        results = client.get(f"/movies/{year}")
        # Verify code first
        assert results.status_code == 200

        # Verify some data
        decoded = json.loads(results.data.decode("utf-8"))
        assert all([type(x) is dict for x in decoded])

