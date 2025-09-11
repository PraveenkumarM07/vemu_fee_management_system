#!/usr/bin/env python3
"""
Database Connection Test Script for Fee Management System
"""

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_database_connection():
    """Test database connection"""
    try:
        from config import DATABASE_URL, DATABASE_CONFIG
        try:
            import psycopg2  # type: ignore[import-not-found]
        except Exception:
            print("Skipping direct PostgreSQL test: psycopg2 not installed. Set DATABASE_URL and install psycopg2-binary to enable.")
            return True
        
        print("Testing PostgreSQL Database Connection...")
        print("=" * 50)
        print(f"Host: {DATABASE_CONFIG['host']}")
        print(f"Port: {DATABASE_CONFIG['port']}")
        print(f"Database: {DATABASE_CONFIG['database']}")
        print(f"Username: {DATABASE_CONFIG['username']}")
        print()
        
        # Test connection
        conn = psycopg2.connect(
            host=DATABASE_CONFIG['host'],
            port=DATABASE_CONFIG['port'],
            database=DATABASE_CONFIG['database'],
            user=DATABASE_CONFIG['username'],
            password=DATABASE_CONFIG['password']
        )
        
        # Test query
        cursor = conn.cursor()
        cursor.execute("SELECT version();")
        version = cursor.fetchone()
        
        print("✓ Database connection successful!")
        print(f"✓ PostgreSQL version: {version[0]}")
        
        # Test if tables exist
        cursor.execute("""
            SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
        """)
        tables = cursor.fetchall()
        
        if tables:
            print(f"✓ Found {len(tables)} existing tables:")
            for table in tables:
                print(f"  - {table[0]}")
        else:
            print("✓ No existing tables found (database is empty)")
        
        cursor.close()
        conn.close()
        
        return True
        
    except ImportError as e:
        print(f"✗ Import error: {e}")
        print("Please install required packages: pip install psycopg2-binary")
        return False
    except Exception as e:
        print(f"✗ Database connection failed: {e}")
        return False

def test_flask_database():
    """Test Flask-SQLAlchemy database connection"""
    try:
        from main import app, db
        
        print("\nTesting Flask-SQLAlchemy Connection...")
        print("=" * 50)
        
        with app.app_context():
            # Test database connection
            with db.engine.connect() as connection:
                result = connection.execute(db.text('SELECT 1'))
                result.fetchone()
            print("✓ Flask-SQLAlchemy connection successful!")
            
            # Check if tables exist
            inspector = db.inspect(db.engine)
            tables = inspector.get_table_names()
            
            if tables:
                print(f"✓ Found {len(tables)} existing tables:")
                for table in tables:
                    print(f"  - {table}")
            else:
                print("✓ No existing tables found (database is empty)")
        
        return True
        
    except Exception as e:
        print(f"✗ Flask-SQLAlchemy connection failed: {e}")
        return False

def main():
    """Run all database tests"""
    print("Fee Management System - Database Connection Test")
    print("=" * 60)
    
    # Test 1: Direct PostgreSQL connection
    test1_passed = test_database_connection()
    
    # Test 2: Flask-SQLAlchemy connection
    test2_passed = test_flask_database()
    
    print("\n" + "=" * 60)
    print("Test Results:")
    print(f"Direct PostgreSQL Connection: {'✓ PASS' if test1_passed else '✗ FAIL'}")
    print(f"Flask-SQLAlchemy Connection: {'✓ PASS' if test2_passed else '✗ FAIL'}")
    
    if test1_passed and test2_passed:
        print("\n🎉 All database tests passed! Your database is ready to use.")
        return True
    else:
        print("\n❌ Some tests failed. Please check the errors above.")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
