#!/usr/bin/env python3
"""
Restaurant Booking System
Startup Script

To run the application:
1. Ensure you have Python installed
2. Install dependencies: pip install -r requirements.txt
3. Run this script: python run.py
4. Open browser to http://localhost:5000

Login Information:
- User Login: Register first, or use sample users (john_doe, jane_smith, ravi_kumar, priya_singh) with password: password123
- Admin Login: Use restaurant name as username (e.g., "Valluvar Restaurant", "Thalapakatti Hotel") with password: admin123
"""

from app import app, init_db, populate_sample_data
import os

def main():
    print("🍽️ Restaurant Booking System")
    print("=" * 40)
    print()
    
    # Check if database exists, if not create it
    if not os.path.exists('restaurant_booking.db'):
        print("Setting up database...")
        init_db()
        populate_sample_data()
        print("✅ Database setup complete!")
    else:
        print("✅ Database found!")
    
    print()
    print("🚀 Starting application...")
    print("📍 URL: http://localhost:5000")
    print()
    print("Login Information:")
    print("👤 Sample Users: john_doe, jane_smith, ravi_kumar, priya_singh")
    print("🔑 User Password: password123")
    print()
    print("👨‍💼 Admin Login:")
    print("🏪 Restaurant Names: Valluvar Restaurant, Thalapakatti Hotel, Saravana Bhavan, Buhari Hotel")
    print("🔑 Admin Password: admin123")
    print()
    print("Press Ctrl+C to stop the server")
    print("=" * 40)
    
    app.run(debug=True, host='0.0.0.0', port=5000)

if __name__ == '__main__':
    main()
