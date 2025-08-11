import os
import secrets


class BaseConfig:
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    DEBUG = True


class ProductionConfig(BaseConfig):
    DEBUG = False


def runtime_settings():
    """
    Returns environment-aware settings evaluated at runtime.

    Security:
        - Generates a strong random SECRET_KEY only if not provided.
    Architecture:
        - Defers env access to runtime (improves testability).
    """
    return {
        "SECRET_KEY": os.environ.get("SECRET_KEY", secrets.token_urlsafe(32)),
        "SQLALCHEMY_DATABASE_URI": os.environ.get(
            "DATABASE_URL", "sqlite:///development.db"
        ),
    }


def get_config_class(name: str):
    mapping = {
        "development": DevelopmentConfig,
        "production": ProductionConfig,
    }
    return mapping.get(name, DevelopmentConfig)


def apply_runtime_env(app):
    """
    Applies runtime (env-based) settings onto the Flask app config.

    Clean Architecture:
        - Separation between static config class and dynamic env overlay.
    """
    app.config.update(runtime_settings())
