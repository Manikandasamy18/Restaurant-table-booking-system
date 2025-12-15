import sqlite3
from datetime import datetime, timedelta

def setup_complete_database():
    """Setup complete database with all tables and comprehensive sample data"""
    conn = sqlite3.connect('restaurant_booking.db')
    
    # Drop existing tables to ensure clean setup
    tables_to_drop = ['special_offers', 'ratings', 'menu_items', 'bookings', 'restaurant_tables', 'restaurants', 'locations', 'users']
    for table in tables_to_drop:
        conn.execute(f'DROP TABLE IF EXISTS {table}')
    
    # Users table
    conn.execute('''
        CREATE TABLE users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Locations table
    conn.execute('''
        CREATE TABLE locations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city_name TEXT UNIQUE NOT NULL
        )
    ''')
    
    # Restaurants table
    conn.execute('''
        CREATE TABLE restaurants (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            location_id INTEGER,
            cuisine_type TEXT NOT NULL,
            is_veg_only INTEGER DEFAULT 0,
            description TEXT,
            image_url TEXT,
            FOREIGN KEY (location_id) REFERENCES locations (id)
        )
    ''')
    
    # Tables in restaurants
    conn.execute('''
        CREATE TABLE restaurant_tables (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            restaurant_id INTEGER,
            table_number TEXT NOT NULL,
            capacity INTEGER NOT NULL,
            is_available INTEGER DEFAULT 1,
            FOREIGN KEY (restaurant_id) REFERENCES restaurants (id)
        )
    ''')
    
    # Bookings table
    conn.execute('''
        CREATE TABLE bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            restaurant_id INTEGER,
            table_id INTEGER,
            booking_date DATE NOT NULL,
            booking_time TIME NOT NULL,
            party_size INTEGER NOT NULL,
            status TEXT DEFAULT 'confirmed',
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (restaurant_id) REFERENCES restaurants (id),
            FOREIGN KEY (table_id) REFERENCES restaurant_tables (id)
        )
    ''')
    
    # Menu items table
    conn.execute('''
        CREATE TABLE menu_items (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            restaurant_id INTEGER,
            item_name TEXT NOT NULL,
            description TEXT,
            price REAL NOT NULL,
            category TEXT NOT NULL,
            is_veg INTEGER DEFAULT 1,
            image_url TEXT,
            FOREIGN KEY (restaurant_id) REFERENCES restaurants (id)
        )
    ''')
    
    # Ratings table
    conn.execute('''
        CREATE TABLE ratings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            restaurant_id INTEGER,
            customer_service INTEGER CHECK(customer_service >= 1 AND customer_service <= 5),
            food_quality INTEGER CHECK(food_quality >= 1 AND food_quality <= 5),
            respect INTEGER CHECK(respect >= 1 AND respect <= 5),
            overall_rating REAL,
            review_text TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id),
            FOREIGN KEY (restaurant_id) REFERENCES restaurants (id)
        )
    ''')
    
    # Special offers table
    conn.execute('''
        CREATE TABLE special_offers (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            restaurant_id INTEGER,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            discount_percentage REAL,
            valid_from DATE,
            valid_to DATE,
            is_active INTEGER DEFAULT 1,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (restaurant_id) REFERENCES restaurants (id)
        )
    ''')
    
    # Insert Tamil Nadu cities
    cities = ['Karur', 'Dindigul', 'Salem', 'Madurai', 'Chennai', 'Coimbatore', 'Trichy', 'Erode']
    for city in cities:
        conn.execute('INSERT INTO locations (city_name) VALUES (?)', (city,))
    
    # Comprehensive restaurant data
    restaurants_data = [
        # Karur restaurants
        {
            'name': 'Valluvar Restaurant',
            'city': 'Karur',
            'cuisine': 'South Indian',
            'is_veg': 1,
            'description': 'Pure vegetarian restaurant with traditional South Indian cuisine and authentic flavors',
            'tables': [('T1', 2), ('T2', 4), ('T3', 6), ('T4', 2), ('T5', 4), ('T6', 6), ('T7', 8), ('T8', 2), ('T9', 4), ('T10', 6)],
            'menu': [
                ('Idli Sambar', 'Steamed rice cakes with aromatic sambar', 50, 'Breakfast', 1),
                ('Masala Dosa', 'Crispy rice crepe with spiced potato filling', 70, 'Breakfast', 1),
                ('Vada', 'Deep fried lentil donuts served with chutney', 40, 'Breakfast', 1),
                ('South Indian Meals', 'Traditional banana leaf meals with variety', 120, 'Lunch', 1),
                ('Curd Rice', 'Rice with yogurt and tempered seasonings', 80, 'Lunch', 1),
                ('Filter Coffee', 'Authentic South Indian filter coffee', 30, 'Beverages', 1)
            ]
        },
        {
            'name': 'Thalapakatti Hotel',
            'city': 'Karur',
            'cuisine': 'Biryani',
            'is_veg': 0,
            'description': 'Famous for authentic Dindigul biryani and traditional non-vegetarian specialties',
            'tables': [('A1', 4), ('A2', 6), ('A3', 2), ('A4', 8), ('A5', 4), ('A6', 6), ('A7', 2), ('A8', 4), ('A9', 6), ('A10', 8)],
            'menu': [
                ('Mutton Biryani', 'Authentic Dindigul style mutton biryani with basmati rice', 280, 'Main Course', 0),
                ('Chicken Biryani', 'Spicy chicken biryani with aromatic spices', 220, 'Main Course', 0),
                ('Veg Biryani', 'Vegetarian biryani with mixed vegetables and saffron', 180, 'Main Course', 1),
                ('Mutton Chukka', 'Dry mutton fry with South Indian spices', 320, 'Main Course', 0),
                ('Chicken 65', 'Spicy fried chicken appetizer', 200, 'Starters', 0),
                ('Egg Biryani', 'Flavorful egg biryani with boiled eggs', 160, 'Main Course', 0)
            ]
        },
        # Chennai restaurants
        {
            'name': 'Saravana Bhavan',
            'city': 'Chennai',
            'cuisine': 'South Indian',
            'is_veg': 1,
            'description': 'World-famous vegetarian restaurant chain serving authentic South Indian cuisine',
            'tables': [('SB1', 2), ('SB2', 4), ('SB3', 6), ('SB4', 2), ('SB5', 4), ('SB6', 6), ('SB7', 8), ('SB8', 2), ('SB9', 4), ('SB10', 6)],
            'menu': [
                ('Rava Dosa', 'Crispy semolina crepe with ghee', 90, 'Breakfast', 1),
                ('Pongal', 'Traditional rice and lentil dish with ghee', 80, 'Breakfast', 1),
                ('Sambar Rice', 'Rice served with traditional sambar curry', 100, 'Lunch', 1),
                ('Rasam Rice', 'Rice with tangy and spicy rasam', 95, 'Lunch', 1),
                ('Payasam', 'Traditional South Indian sweet dessert', 60, 'Desserts', 1),
                ('Buttermilk', 'Refreshing spiced buttermilk', 40, 'Beverages', 1)
            ]
        },
        {
            'name': 'Buhari Hotel',
            'city': 'Chennai',
            'cuisine': 'Multi-cuisine',
            'is_veg': 0,
            'description': 'Heritage restaurant established in 1951, serving both vegetarian and non-vegetarian dishes',
            'tables': [('BH1', 4), ('BH2', 6), ('BH3', 2), ('BH4', 8), ('BH5', 4), ('BH6', 6), ('BH7', 2), ('BH8', 4), ('BH9', 6), ('BH10', 8)],
            'menu': [
                ('Chicken Biryani', 'Traditional Chennai style chicken biryani', 240, 'Main Course', 0),
                ('Mutton Curry', 'Spicy mutton curry with traditional spices', 320, 'Main Course', 0),
                ('Fish Curry', 'South Indian style fish curry with coconut', 280, 'Main Course', 0),
                ('Veg Fried Rice', 'Fried rice with mixed vegetables', 140, 'Main Course', 1),
                ('Paneer Butter Masala', 'Rich paneer in creamy tomato gravy', 200, 'Main Course', 1),
                ('Chicken Tikka', 'Grilled chicken pieces with spices', 220, 'Starters', 0)
            ]
        },
        # Madurai restaurants
        {
            'name': 'Anjappar',
            'city': 'Madurai',
            'cuisine': 'Chettinad',
            'is_veg': 0,
            'description': 'Authentic Chettinad cuisine restaurant famous for spicy and flavorful dishes',
            'tables': [('C1', 4), ('C2', 6), ('C3', 2), ('C4', 8), ('C5', 4), ('C6', 6), ('C7', 2), ('C8', 4)],
            'menu': [
                ('Chettinad Chicken', 'Spicy Chettinad style chicken curry', 260, 'Main Course', 0),
                ('Mutton Sukka', 'Dry mutton preparation with Chettinad spices', 340, 'Main Course', 0),
                ('Fish Fry', 'Crispy fried fish with Chettinad masala', 220, 'Starters', 0),
                ('Veg Kurma', 'Mixed vegetable curry in coconut gravy', 160, 'Main Course', 1),
                ('Pepper Chicken', 'Black pepper flavored chicken', 240, 'Main Course', 0)
            ]
        },
        {
            'name': 'Meenakshi Bhavan',
            'city': 'Madurai',
            'cuisine': 'South Indian',
            'is_veg': 1,
            'description': 'Traditional vegetarian restaurant serving temple city authentic flavors',
            'tables': [('MB1', 2), ('MB2', 4), ('MB3', 6), ('MB4', 2), ('MB5', 4), ('MB6', 6), ('MB7', 8), ('MB8', 2)],
            'menu': [
                ('Temple Special Meals', 'Traditional temple style vegetarian meals', 140, 'Lunch', 1),
                ('Madurai Idli', 'Soft steamed rice cakes temple style', 60, 'Breakfast', 1),
                ('Jigarthanda', 'Famous Madurai cold beverage', 80, 'Beverages', 1),
                ('Kootu', 'Mixed vegetable and lentil curry', 90, 'Lunch', 1),
                ('Appam', 'Fermented rice pancakes', 70, 'Breakfast', 1)
            ]
        }
    ]
    
    # Insert all restaurant data
    for restaurant_data in restaurants_data:
        # Get location ID
        location = conn.execute('SELECT id FROM locations WHERE city_name = ?', (restaurant_data['city'],)).fetchone()
        if location:
            location_id = location[0]
            
            # Insert restaurant
            conn.execute('''INSERT INTO restaurants 
                           (name, location_id, cuisine_type, is_veg_only, description) 
                           VALUES (?, ?, ?, ?, ?)''', 
                          (restaurant_data['name'], location_id, restaurant_data['cuisine'], 
                           restaurant_data['is_veg'], restaurant_data['description']))
            
            # Get restaurant ID
            restaurant = conn.execute('SELECT id FROM restaurants WHERE name = ?', (restaurant_data['name'],)).fetchone()
            if restaurant:
                restaurant_id = restaurant[0]
                
                # Insert tables
                for table_data in restaurant_data['tables']:
                    conn.execute('INSERT INTO restaurant_tables (restaurant_id, table_number, capacity) VALUES (?, ?, ?)',
                               (restaurant_id, table_data[0], table_data[1]))
                
                # Insert menu items
                for menu_item in restaurant_data['menu']:
                    conn.execute('''INSERT INTO menu_items 
                                   (restaurant_id, item_name, description, price, category, is_veg) 
                                   VALUES (?, ?, ?, ?, ?, ?)''',
                               (restaurant_id, menu_item[0], menu_item[1], menu_item[2], menu_item[3], menu_item[4]))
    
    # Insert sample users
    sample_users = [
        ('john_doe', 'password123', 'john@email.com', '9876543210'),
        ('jane_smith', 'password123', 'jane@email.com', '9876543211'),
        ('ravi_kumar', 'password123', 'ravi@email.com', '9876543212'),
        ('priya_singh', 'password123', 'priya@email.com', '9876543213')
    ]
    
    for user_data in sample_users:
        conn.execute('INSERT INTO users (username, password, email, phone) VALUES (?, ?, ?, ?)', user_data)
    
    # Insert sample special offers
    today = datetime.now().date()
    next_month = today + timedelta(days=30)
    
    # Get restaurant IDs for offers
    valluvar = conn.execute('SELECT id FROM restaurants WHERE name = "Valluvar Restaurant"').fetchone()
    thalapakatti = conn.execute('SELECT id FROM restaurants WHERE name = "Thalapakatti Hotel"').fetchone()
    
    if valluvar:
        conn.execute('''INSERT INTO special_offers 
                       (restaurant_id, title, description, discount_percentage, valid_from, valid_to) 
                       VALUES (?, ?, ?, ?, ?, ?)''',
                    (valluvar[0], 'Weekend Special', 'Get 15% off on all South Indian breakfast items during weekends', 
                     15, today, next_month))
    
    if thalapakatti:
        conn.execute('''INSERT INTO special_offers 
                       (restaurant_id, title, description, discount_percentage, valid_from, valid_to) 
                       VALUES (?, ?, ?, ?, ?, ?)''',
                    (thalapakatti[0], 'Biryani Festival', 'Special 20% discount on all biryani varieties', 
                     20, today, next_month))
    
    conn.commit()
    conn.close()
    print("Complete database setup finished successfully!")
    print("Sample restaurants created in Karur, Chennai, and Madurai")
    print("Sample users created with password: password123")
    print("Admin access: Use restaurant name as username and 'admin123' as password")

if __name__ == '__main__':
    setup_complete_database()
