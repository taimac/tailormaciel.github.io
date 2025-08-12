from flask import Flask, jsonify
from backend import config as cfg


def create_app(config_name="development"):
    """
    Application factory for creating Flask app instances.

    Args:
        config_name (str): The configuration to use ('development' or 'production').

    Returns:
        Flask: Configured Flask application instance.

    Security Notes:
        - Loads config from config.py, supporting separation of secrets
        - Input validation prevents configuration injection attacks
        - Enables different settings for dev/prod environments

    Architecture Notes:
        - Follows Clean Architecture: separates app creation from running
        - Implements Factory Pattern for object creation
        - Supports dependency injection for blueprints/extensions

    OOP Principles Applied:
        - Factory Pattern: Encapsulates complex object creation logic
        - Single Responsibility: Only handles app creation and configuration
        - Encapsulation: Configuration logic hidden from caller

    Teaching Benefits:
        - Demonstrates secure configuration management
        - Shows proper error handling with descriptive messages
        - Illustrates Clean Architecture dependency direction
    """
    app = Flask(__name__)
    config_class = cfg.get_config_class(config_name)
    app.config.from_object(config_class)
    cfg.apply_runtime_env(app)

    # Register blueprints here (add as you implement features)
    # from controllers import auth_bp, content_bp
    # app.register_blueprint(auth_bp)
    # app.register_blueprint(content_bp)

    # Health check endpoint
    @app.route("/health", methods=["GET"])
    def health():
        """
        Basic health check endpoint.

        Returns:
            JSON indicating service status.

        Security Notes:
            - Does not expose sensitive system information
            - No authentication required (public health check)
            - Response format prevents information disclosure

        Architecture Notes:
            - Stateless endpoint following REST principles
            - Minimal response for performance and security

        Teaching Points:
            - Demonstrates proper endpoint design
            - Shows security-conscious response formatting
            - Illustrates separation of health check from business logic
        """
        return jsonify({"status": "ok"}), 200

    return app


if __name__ == "__main__":
    app = create_app("development")
    app.run(debug=True)
