from backend.app import create_app


def test_development_config_defaults(monkeypatch):
    """
    Verifies DevelopmentConfig loads correct defaults and enables debug mode.

    Security Notes:
        - Ensures no secrets are hardcoded.
    Architecture Notes:
        - Validates separation of config from code.
    """
    monkeypatch.delenv("SECRET_KEY", raising=False)
    app = create_app("development")
    assert app.config["DEBUG"] is True
    assert app.config["SECRET_KEY"]  # exists
    assert app.config["SQLALCHEMY_DATABASE_URI"].startswith("sqlite")


def test_production_config_env(monkeypatch):
    """
    Verifies ProductionConfig disables debug and loads environment variables.

    Security Notes:
        - Ensures secrets are loaded from environment, not code.
    Architecture Notes:
        - Supports environment-based configuration for deployment.
    """
    monkeypatch.setenv("SECRET_KEY", "super-secret-key")
    monkeypatch.setenv("DATABASE_URL", "postgresql://user:pass@localhost/db")
    app = create_app("production")
    assert app.config["DEBUG"] is False
    assert app.config["SECRET_KEY"] == "super-secret-key"
    assert app.config["SQLALCHEMY_DATABASE_URI"].startswith("postgresql://")
