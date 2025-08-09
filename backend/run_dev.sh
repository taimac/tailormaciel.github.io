#!/bin/bash
# filepath: backend/run_dev.sh

# Activate virtual environment
source .venv/bin/activate

# Export environment variables for development
export FLASK_DEBUG=1
export FLASK_APP=app.py

# Optional: load secrets from .env if using python-dotenv
# export $(grep -v '^#' .env | xargs)

# Start the Flask development server
python app.py