#!/usr/bin/env python3
"""
Setup script for Fee Management System
This script installs all required dependencies and sets up the application
"""

import subprocess
import sys
import os

def install_requirements():
    """Install required packages from requirements.txt"""
    try:
        print("Installing required packages...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✓ All packages installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error installing packages: {e}")
        return False

def test_installation():
    """Test if the installation was successful"""
    try:
        import flask
        import flask_sqlalchemy
        import flask_migrate
        import flask_cors
        print("✓ All required modules imported successfully")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def main():
    """Main setup function"""
    print("Fee Management System Setup")
    print("=" * 40)
    
    # Install requirements
    if not install_requirements():
        print("Setup failed: Could not install requirements")
        return False
    
    print()
    
    # Test installation
    if not test_installation():
        print("Setup failed: Installation test failed")
        return False
    
    print()
    print("=" * 40)
    print("✓ Setup completed successfully!")
    print()
    print("Next steps:")
    print("1. Run the application using: python main.py")
    print("2. Or use the batch file: run_app.bat")
    print("3. Open your browser and go to: http://localhost:5000")
    print()
    print("Default login credentials:")
    print("- Admin: admin@example.com / admin123")
    print("- Employee: vemuit@gmail.com / vemuit@2008")
    print("- Student password: vemuit@2008")
    
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
