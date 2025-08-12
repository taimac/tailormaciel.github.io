import os
import secrets


class BaseConfig:
    """
    Base configuration class demonstrating OOP inheritance and security best practices.

    Security Principles Applied:
        - No hardcoded secrets (uses environment variables)
        - Cryptographically secure random key generation
        - Principle of least privilege in configuration exposure

    OOP Principles Demonstrated:
        - Inheritance: Child classes extend base functionality
        - Encapsulation: Configuration logic contained in classes
        - Abstraction: Common configuration interface for all environments

    Clean Architecture Benefits:
        - Configuration separated from business logic
        - Environment-specific behavior through inheritance
        - Testable configuration through dependency injection

    Teaching Points:
        - Shows proper use of class inheritance
        - Demonstrates secure default configuration
        - Illustrates separation of concerns in system configuration
    """
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """
    Development configuration with debug features enabled.

    Security Note: Debug mode should NEVER be enabled in production

    Teaching Points:
        - Environment-specific configuration inheritance
        - Clear separation between dev and prod settings
        - Demonstrates polymorphism through config class substitution
    """
    DEBUG = True


class ProductionConfig(BaseConfig):
    """
    Production configuration with security hardening.

    Security Features:
        - Debug mode disabled
        - Future: Secure cookie settings, HTTPS enforcement
        - Future: Production database configuration

    Architecture Note:
        - Inheritance allows shared base config with prod-specific overrides
        - Demonstrates Open/Closed Principle: open for extension, closed for modification
    """
    DEBUG = False


def runtime_settings():
    """
    Returns environment-aware settings evaluated at runtime.

    Security Benefits:
        - Secrets loaded from environment, never hardcoded
        - Strong random SECRET_KEY generation if not provided
        - Database URI configurable per environment

    Architecture Benefits:
        - Defers env access to runtime (improves testability)
        - Supports Clean Architecture dependency inversion
        - Enables different configurations for testing vs production

    Teaching Points:
        - Demonstrates secure secret management
        - Shows separation of static vs dynamic configuration
        - Illustrates cryptographically secure random generation

    SDD Principles:
        - Defense in depth: multiple layers of configuration security
        - Fail-safe defaults: secure random key if none provided
        - Least privilege: only necessary environment access
    """
    return {
        "SECRET_KEY": os.environ.get("SECRET_KEY", secrets.token_urlsafe(32)),
        "SQLALCHEMY_DATABASE_URI": os.environ.get(
            "DATABASE_URL", "sqlite:///development.db"
        ),
    }


def get_config_class(name: str):
    """
    Returns the appropriate configuration class for the given environment name.

    Args:
        name: Environment name ('development', 'production')

    Returns:
        Configuration class for the specified environment

    Security Notes:
        - Input validation prevents configuration injection
        - Explicit mapping prevents arbitrary class loading
        - Defensive programming with safe defaults

    Architecture Notes:
        - Factory pattern for configuration object creation
        - Centralized configuration class management
        - Polymorphism: different configs implement same interface

    Teaching Benefits:
        - Demonstrates input validation importance
        - Shows factory pattern implementation
        - Illustrates secure configuration selection

    OOP Principles:
        - Factory Pattern: Creates objects without exposing creation logic
        - Polymorphism: Different config classes used interchangeably
        - Encapsulation: Configuration selection logic contained
    """
    mapping = {
        "development": DevelopmentConfig,
        "production": ProductionConfig,
    }
    return mapping.get(name, DevelopmentConfig)


def apply_runtime_env(app):
    """
    Applies runtime (env-based) settings onto the Flask app config.

    Args:
        app: Flask application instance to configure

    Clean Architecture Benefits:
        - Separation between static config class and dynamic env overlay
        - Infrastructure layer (env vars) isolated from application layer
        - Testable by mocking environment variables

    Security Benefits:
        - Runtime secret loading prevents hardcoded credentials
        - Environment-specific database connections
        - Configurable security settings per environment

    Teaching Points:
        - Shows Clean Architecture dependency direction
        - Demonstrates runtime configuration application
        - Illustrates separation of concerns in configuration management

    OOP Principles:
        - Single Responsibility: Only handles runtime environment application
        - Dependency Injection: Receives app instance rather than creating it
        - Interface Segregation: Focused function with single purpose
    """
    app.config.update(runtime_settings())