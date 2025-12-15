import sqlite3

def populate_sample_data():
    """Populate database with comprehensive sample data"""
    conn = sqlite3.connect('restaurant_booking.db')
    
    # Sample restaurants with tables and menu items
    restaurants_with_data = [
        {
            'name': 'Valluvar Restaurant',
            'city': 'Karur',
            'cuisine': 'South Indian',
            'is_veg': 1,
            'description': 'Pure vegetarian restaurant with traditional South Indian cuisine',
            'tables': [
                ('T1', 2), ('T2', 4), ('T3', 6), ('T4', 2), ('T5', 4),
                ('T6', 6), ('T7', 8), ('T8', 2), ('T9', 4), ('T10', 6)
            ],
            'menu': [
                ('Idli Sambar', 'Steamed rice cakes with sambar', 50, 'Breakfast', 1),
                ('Dosa', 'Crispy rice crepe', 60, 'Breakfast', 1),
                ('Vada', 'Deep fried lentil donuts', 40, 'Breakfast', 1),
                ('Meals', 'Traditional South Indian thali', 120, 'Lunch', 1),
                ('Curd Rice', 'Rice with yogurt and seasonings', 80, 'Lunch', 1)
            ]
        },
        {
            'name': 'Thalapakatti Hotel',
            'city': 'Karur',
            'cuisine': 'Biryani',
            'is_veg': 0,
            'description': 'Famous for authentic Dindigul biryani and non-veg specialties',
            'tables': [
                ('A1', 4), ('A2', 6), ('A3', 2), ('A4', 8), ('A5', 4),
                ('A6', 6), ('A7', 2), ('A8', 4), ('A9', 6), ('A10', 8)
            ],
            'menu': [
                ('Mutton Biryani', 'Authentic Dindigul style mutton biryani', 250, 'Main Course', 0),
                ('Chicken Biryani', 'Spicy chicken biryani', 200, 'Main Course', 0),
                ('Veg Biryani', 'Vegetarian biryani with mixed vegetables', 150, 'Main Course', 1),
                ('Mutton Chukka', 'Dry mutton fry', 280, 'Main Course', 0),
                ('Chicken 65', 'Spicy fried chicken appetizer', 180, 'Starters', 0)
            ]
        },
        {
            'name': 'Saravana Bhavan',
            'city': 'Chennai',
            'cuisine': 'South Indian',
            'is_veg': 1,
            'description': 'Popular vegetarian chain restaurant',
            'tables': [
                ('SB1', 2), ('SB2', 4), ('SB3', 6), ('SB4', 2), ('SB5', 4),
                ('SB6', 6), ('SB7', 8), ('SB8', 2), ('SB9', 4), ('SB10', 6)
            ],
            'menu': [
                ('Rava Dosa', 'Crispy semolina crepe', 80, 'Breakfast', 1),
                ('Filter Coffee', 'Traditional South Indian coffee', 30, 'Beverages', 1),
                ('Pongal', 'Rice and lentil dish', 70, 'Breakfast', 1),
                ('Sambar Rice', 'Rice with sambar gravy', 90, 'Lunch', 1),
                ('Rasam Rice', 'Rice with tangy rasam', 85, 'Lunch', 1)
            ]
        },
        {
            'name': 'Buhari Hotel',
            'city': 'Chennai',
            'cuisine': 'Multi-cuisine',
            'is_veg': 0,
            'description': 'Heritage restaurant serving both veg and non-veg dishes',
            'tables': [
                ('BH1', 4), ('BH2', 6), ('BH3', 2), ('BH4', 8), ('BH5', 4),
                ('BH6', 6), ('BH7', 2), ('BH8', 4), ('BH9', 6), ('BH10', 8)
            ],
            'menu': [
                ('Chicken Biryani', 'Traditional Chennai style biryani', 220, 'Main Course', 0),
                ('Mutton Curry', 'Spicy mutton curry', 300, 'Main Course', 0),
                ('Veg Fried Rice', 'Fried rice with vegetables', 120, 'Main Course', 1),
                ('Fish Curry', 'South Indian style fish curry', 250, 'Main Course', 0),
                ('Paneer Butter Masala', 'Rich paneer in tomato gravy', 180, 'Main Course', 1)
            ]
        }
    ]
    
    # Insert sample data
    for restaurant_data in restaurants_with_data:
        # Get location ID
        location = conn.execute('SELECT id FROM locations WHERE city_name = ?', (restaurant_data['city'],)).fetchone()
        if location:
            location_id = location[0]
            
            # Insert restaurant
            cursor = conn.execute('''INSERT OR IGNORE INTO restaurants 
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
                    conn.execute('INSERT OR IGNORE INTO restaurant_tables (restaurant_id, table_number, capacity) VALUES (?, ?, ?)',
                               (restaurant_id, table_data[0], table_data[1]))
                
                # Insert menu items
                for menu_item in restaurant_data['menu']:
                    conn.execute('''INSERT OR IGNORE INTO menu_items 
                                   (restaurant_id, item_name, description, price, category, is_veg) 
                                   VALUES (?, ?, ?, ?, ?, ?)''',
                               (restaurant_id, menu_item[0], menu_item[1], menu_item[2], menu_item[3], menu_item[4]))
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    populate_sample_data()
    print("Sample data populated successfully!")
