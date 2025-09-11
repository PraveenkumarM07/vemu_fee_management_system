#!/usr/bin/env python3
"""
Test script to verify the Flask application works correctly
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_imports():
    """Test if all imports work correctly"""
    try:
        from main import app, db, User, Student, Transaction, Complaint
        print("✓ All imports successful")
        return True
    except ImportError as e:
        print(f"✗ Import error: {e}")
        return False

def test_app_creation():
    """Test if Flask app is created correctly"""
    try:
        from main import app
        print("✓ Flask app created successfully")
        print(f"✓ App name: {app.name}")
        print(f"✓ Debug mode: {app.debug}")
        return True
    except Exception as e:
        print(f"✗ App creation error: {e}")
        return False

def test_database_models():
    """Test if database models are defined correctly"""
    try:
        from main import User, Student, Transaction, Complaint
        
        # Test User model
        user_attrs = ['id', 'username', 'email', 'password_hash', 'role']
        for attr in user_attrs:
            if not hasattr(User, attr):
                print(f"✗ User model missing attribute: {attr}")
                return False
        
        # Test Student model
        student_attrs = ['id', 'name', 'roll_number', 'total_fees', 'paid_amount']
        for attr in student_attrs:
            if not hasattr(Student, attr):
                print(f"✗ Student model missing attribute: {attr}")
                return False
        
        print("✓ All database models defined correctly")
        return True
    except Exception as e:
        print(f"✗ Database model error: {e}")
        return False

def test_routes():
    """Test if routes are defined correctly"""
    try:
        from main import app
        
        # Get all routes
        routes = []
        for rule in app.url_map.iter_rules():
            routes.append(rule.rule)
        
        expected_routes = ['/', '/studentlogin', '/employlogin', '/dashboard']
        for route in expected_routes:
            if route not in routes:
                print(f"✗ Missing route: {route}")
                return False
        
        print("✓ All expected routes defined")
        print(f"✓ Total routes: {len(routes)}")
        return True
    except Exception as e:
        print(f"✗ Route test error: {e}")
        return False

def main():
    """Run all tests"""
    print("Testing Flask Fee Management System...")
    print("=" * 50)
    
    tests = [
        test_imports,
        test_app_creation,
        test_database_models,
        test_routes
    ]
    
    passed = 0
    total = len(tests)
    
    for test in tests:
        if test():
            passed += 1
        print()
    
    print("=" * 50)
    print(f"Tests passed: {passed}/{total}")
    
    if passed == total:
        print("✓ All tests passed! Application is ready to run.")
        return True
    else:
        print("✗ Some tests failed. Please check the errors above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
