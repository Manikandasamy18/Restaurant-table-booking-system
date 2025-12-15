#!/usr/bin/env python3
"""
Simple test script to verify the restaurant booking system
"""

import sqlite3
import os
from app import app

def test_database():
    """Test database connectivity and data"""
    print("🔍 Testing database...")
    
    if not os.path.exists('restaurant_booking.db'):
        print("❌ Database not found! Run setup_database.py first.")
        return False
    
    conn = sqlite3.connect('restaurant_booking.db')
    conn.row_factory = sqlite3.Row
    
    # Test locations
    locations = conn.execute('SELECT * FROM locations').fetchall()
    print(f"✅ Found {len(locations)} locations: {[loc['city_name'] for loc in locations]}")
    
    # Test restaurants
    restaurants = conn.execute('SELECT * FROM restaurants').fetchall()
    print(f"✅ Found {len(restaurants)} restaurants")
    
    # Test users
    users = conn.execute('SELECT * FROM users').fetchall()
    print(f"✅ Found {len(users)} sample users")
    
    # Test menu items
    menu_items = conn.execute('SELECT * FROM menu_items').fetchall()
    print(f"✅ Found {len(menu_items)} menu items")
    
    # Test tables
    tables = conn.execute('SELECT * FROM restaurant_tables').fetchall()
    print(f"✅ Found {len(tables)} restaurant tables")
    
    conn.close()
    return True

def test_routes():
    """Test Flask routes"""
    print("\n🌐 Testing Flask routes...")
    
    with app.test_client() as client:
        # Test home page
        response = client.get('/')
        print(f"✅ Home page: Status {response.status_code}")
        
        # Test login page
        response = client.get('/login')
        print(f"✅ Login page: Status {response.status_code}")
        
        # Test register page
        response = client.get('/register')
        print(f"✅ Register page: Status {response.status_code}")
        
        # Test admin login page
        response = client.get('/admin-login')
        print(f"✅ Admin login page: Status {response.status_code}")

def main():
    print("🍽️ Restaurant Booking System - Test Suite")
    print("=" * 50)
    
    if test_database():
        test_routes()
        print("\n🎉 All tests passed! The application is ready to use.")
        print("\n📋 To start the application:")
        print("   python run.py")
        print("\n🌐 Then open: http://localhost:5000")
        print("\n👤 Sample login:")
        print("   Username: john_doe")
        print("   Password: password123")
        print("\n👨‍💼 Admin login:")
        print("   Restaurant: Valluvar Restaurant")
        print("   Password: admin123")
    else:
        print("\n❌ Database test failed. Please run setup_database.py first.")

if __name__ == '__main__':
    main()
