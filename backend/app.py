from flask import Flask, jsonify

def create_app(config_name='development'):
    """
    Application factory for creating Flask app instances.

    Args:
        config_name (str): The configuration to use ('development' or 'production').

    Returns:
        Flask: Configured Flask application instance.

    Security Notes:
        - Loads config from config.py, supporting separation of secrets.
        - Enables different settings for dev/prod environments.
    Architecture Notes:
        - Follows Clean Architecture: separates app creation from running.
        - Supports dependency injection for blueprints/extensions.
    """
    app = Flask(__name__)

    # Load configuration
    # Load configuration using a validated mapping
    config_mapping = {
        'development': 'config.DevelopmentConfig',
        'production': 'config.ProductionConfig'
    }
    config_class = config_mapping.get(config_name.lower())
    if not config_class:
        raise ValueError(f"Invalid config_name '{config_name}'. Allowed values are: {list(config_mapping.keys())}")
    app.config.from_object(config_class)

    # Register blueprints here (add as you implement features)
    # from controllers import auth_bp, content_bp
    # app.register_blueprint(auth_bp)
    # app.register_blueprint(content_bp)

    # Health check endpoint
    @app.route('/health', methods=['GET'])
    def health():
        """
        Basic health check endpoint.

        Returns:
            JSON indicating service status.

        Security Notes:
            - Does not expose sensitive info.
        """
        return jsonify({"status": "ok"}), 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)