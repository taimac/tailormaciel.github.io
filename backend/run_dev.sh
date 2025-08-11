#!/bin/bash
# filepath: backend/run_dev.sh

# Activate virtual environment
if [ -f ".venv/bin/activate" ]; then
    source .venv/bin/activate
elif [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
else
    echo "Error: No virtual environment found in .venv or venv."
    exit 1
fi

# Export environment variables for development
export FLASK_DEBUG=1
export FLASK_APP=app.py

# Optional: load secrets from .env if using python-dotenv
# export $(grep -v '^#' .env | xargs)

# Start the Flask development server
python app.py