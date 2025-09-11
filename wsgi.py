"""
WSGI entry point for production deployment (Render)
"""

import os
import sys

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import app, init_db

# Initialize database on startup
try:
    init_db()
    print("✓ Database initialized successfully")
except Exception as e:
    print(f"⚠️ Database initialization warning: {e}")
    print("✓ Continuing with existing database state...")

# Export the Flask app for Gunicorn
application = app

if __name__ == "__main__":
    app.run(debug=False, host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
