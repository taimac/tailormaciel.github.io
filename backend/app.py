from flask import Flask, jsonify
from backend import config as cfg

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
    config_class = cfg.get_config_class(config_name)
    app.config.from_object(config_class)
    cfg.apply_runtime_env(app)

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
    app = create_app('development')
    app.run(debug=True)