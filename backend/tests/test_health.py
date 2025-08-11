def test_health_endpoint_ok(client):
    """
    Verifies the /health endpoint responds with status 200 and correct payload.

    Security Notes:
        - Ensures endpoint does not leak sensitive info.
    Architecture Notes:
        - Validates application factory and test client integration.
        - Demonstrates separation of concerns (endpoint logic vs. test logic).
    """
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}
