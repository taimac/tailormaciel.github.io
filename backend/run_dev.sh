#!/bin/bash
# Development server startup script with comprehensive error handling and validation

echo "🚀 Starting Flask Development Environment..."

# Activate virtual environment with robust error checking
if [ -f ".venv/bin/activate" ]; then
    echo "✅ Activating .venv virtual environment"
    source .venv/bin/activate
elif [ -f "venv/bin/activate" ]; then
    echo "✅ Activating venv virtual environment"
    source venv/bin/activate
else
    echo "❌ Error: No virtual environment found in .venv or venv."
    echo "📝 Please create one with: python -m venv .venv"
    echo "📝 Then install dependencies: pip install -r requirements.txt"
    exit 1
fi

# Validate Python environment
if ! command -v python &> /dev/null; then
    echo "❌ Error: Python not found in virtual environment"
    exit 1
fi

# Export environment variables for development
export FLASK_DEBUG=1    # More explicit than deprecated FLASK_ENV
export FLASK_APP=app.py

echo "🔧 Environment Configuration:"
echo "   - FLASK_DEBUG: $FLASK_DEBUG"
echo "   - FLASK_APP: $FLASK_APP"
echo "   - Virtual Environment: Activated"

# Optional: load secrets from .env if using python-dotenv
# if [ -f ".env" ]; then
#     echo "📝 Loading environment variables from .env"
#     export $(grep -v '^#' .env | xargs)
# fi

# Validate that Flask is available
if ! python -c "import flask" 2>/dev/null; then
    echo "❌ Error: Flask not installed in virtual environment."
    echo "📝 Please run: pip install -r requirements.txt"
    exit 1
fi

# Validate that our application module can be imported
if ! python -c "from backend.app import create_app" 2>/dev/null; then
    echo "❌ Error: Cannot import application. Check for syntax errors."
    echo "📝 Run: python -m py_compile backend/app.py"
    exit 1
fi

echo "✅ All validations passed"
echo "🌐 Starting Flask development server..."
echo "📍 Server will be available at: http://127.0.0.1:5000"
echo "🔍 Health check endpoint: http://127.0.0.1:5000/health"
echo "⏹️  Press Ctrl+C to stop the server"
echo ""

# Start the Flask development server
python app.py