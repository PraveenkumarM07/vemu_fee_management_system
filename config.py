"""
Database Configuration for Fee Management System
"""

import os

# Database Configuration
DATABASE_CONFIG = {
    'host': 'dpg-d31353d6ubrc73c1jfmg-a.oregon-postgres.render.com',
    'port': 5432,
    'database': 'vemu_fee',
    'username': 'vemu_fee_user',
    'password': 'SoaqripTGHMX16rb79Jyylq60CiF6Z1Z'
}

# Construct database URL
DATABASE_URL = f"postgresql://{DATABASE_CONFIG['username']}:{DATABASE_CONFIG['password']}@{DATABASE_CONFIG['host']}/{DATABASE_CONFIG['database']}"

# Flask Configuration
SECRET_KEY = os.environ.get('SECRET_KEY', 'your-secret-key-here-change-in-production')
FLASK_ENV = os.environ.get('FLASK_ENV', 'development')

# Print database connection info (for debugging)
def print_db_info():
    print("Database Configuration:")
    print(f"  Host: {DATABASE_CONFIG['host']}")
    print(f"  Port: {DATABASE_CONFIG['port']}")
    print(f"  Database: {DATABASE_CONFIG['database']}")
    print(f"  Username: {DATABASE_CONFIG['username']}")
    print(f"  URL: {DATABASE_URL[:50]}...")  # Show only first 50 chars for security

if __name__ == "__main__":
    print_db_info()
