from app import get_status_code, is_successful_status


class DummyResponse:
    status_code = 200


def test_get_status_code(monkeypatch):
    def fake_get(url, timeout=5):
        return DummyResponse()

    monkeypatch.setattr("app.requests.get", fake_get)
    assert get_status_code("https://example.com") == 200


def test_is_successful_status():
    assert is_successful_status(200) is True
    assert is_successful_status(204) is True
    assert is_successful_status(301) is False
    assert is_successful_status(404) is False
    assert is_successful_status(500) is False
