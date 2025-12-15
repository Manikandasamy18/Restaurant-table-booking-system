from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
import sqlite3
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Database configuration
DATABASE = 'restaurant_booking.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """Initialize database with all required tables"""
    conn = get_db_connection()
    
    # Users table
    conn.execute('''
        CREATE TABLE IF NOT EXISTS users (
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
        CREATE TABLE IF NOT EXISTS locations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            city_name TEXT UNIQUE NOT NULL
        )
    ''')
    
    # Restaurants table
    conn.execute('''
        CREATE TABLE IF NOT EXISTS restaurants (
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
        CREATE TABLE IF NOT EXISTS restaurant_tables (
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
        CREATE TABLE IF NOT EXISTS bookings (
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
        CREATE TABLE IF NOT EXISTS menu_items (
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
        CREATE TABLE IF NOT EXISTS ratings (
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
        CREATE TABLE IF NOT EXISTS special_offers (
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
    
    conn.commit()
    conn.close()

def populate_sample_data():
    """Populate database with sample data"""
    conn = get_db_connection()
    
    # Insert Tamil Nadu cities
    cities = ['Karur', 'Dindigul', 'Salem', 'Madurai', 'Chennai', 'Coimbatore', 'Trichy', 'Erode']
    for city in cities:
        conn.execute('INSERT OR IGNORE INTO locations (city_name) VALUES (?)', (city,))
    
    # Sample restaurants for different cities
    restaurants_data = [
        ('Valluvar Restaurant', 'Karur', 'South Indian', 1, 'Pure vegetarian restaurant with traditional South Indian cuisine'),
        ('Thalapakatti Hotel', 'Karur', 'Biryani', 0, 'Famous for authentic Dindigul biryani and non-veg specialties'),
        ('Saravana Bhavan', 'Chennai', 'South Indian', 1, 'Popular vegetarian chain restaurant'),
        ('Buhari Hotel', 'Chennai', 'Multi-cuisine', 0, 'Heritage restaurant serving both veg and non-veg dishes'),
        ('Anjappar', 'Madurai', 'Chettinad', 0, 'Authentic Chettinad cuisine restaurant'),
        ('Meenakshi Bhavan', 'Madurai', 'South Indian', 1, 'Traditional vegetarian restaurant'),
        ('Hotel Junior Kuppanna', 'Salem', 'South Indian', 0, 'Famous for South Indian non-veg dishes'),
        ('Shree Annapoorna', 'Salem', 'South Indian', 1, 'Popular vegetarian restaurant chain')
    ]
    
    for restaurant_data in restaurants_data:
        # Get location_id
        location = conn.execute('SELECT id FROM locations WHERE city_name = ?', (restaurant_data[1],)).fetchone()
        if location:
            conn.execute('''INSERT OR IGNORE INTO restaurants 
                           (name, location_id, cuisine_type, is_veg_only, description) 
                           VALUES (?, ?, ?, ?, ?)''', 
                          (restaurant_data[0], location['id'], restaurant_data[2], restaurant_data[3], restaurant_data[4]))
    
    conn.commit()
    conn.close()

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        phone = request.form['phone']
        
        conn = get_db_connection()
        try:
            conn.execute('INSERT INTO users (username, password, email, phone) VALUES (?, ?, ?, ?)',
                        (username, password, email, phone))
            conn.commit()
            flash('Registration successful! Please login.')
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            flash('Username already exists!')
        finally:
            conn.close()
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ? AND password = ?',
                           (username, password)).fetchone()
        conn.close()
        
        if user:
            session['user_id'] = user['id']
            session['username'] = user['username']
            return redirect(url_for('select_location'))
        else:
            flash('Invalid username or password!')
    
    return render_template('login.html')

@app.route('/admin-login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        restaurant_name = request.form['restaurant_name']
        password = request.form['password']
        
        if password == 'admin123':
            conn = get_db_connection()
            restaurant = conn.execute('SELECT * FROM restaurants WHERE name = ?', (restaurant_name,)).fetchone()
            conn.close()
            
            if restaurant:
                session['admin_restaurant_id'] = restaurant['id']
                session['admin_restaurant_name'] = restaurant['name']
                return redirect(url_for('admin_dashboard'))
            else:
                flash('Restaurant not found!')
        else:
            flash('Invalid password!')
    
    return render_template('admin_login.html')

@app.route('/select-location')
def select_location():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    conn = get_db_connection()
    locations = conn.execute('SELECT * FROM locations ORDER BY city_name').fetchall()
    conn.close()
    
    return render_template('select_location.html', locations=locations)

@app.route('/restaurants/<int:location_id>')
def restaurants_by_location(location_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    conn = get_db_connection()
    location = conn.execute('SELECT * FROM locations WHERE id = ?', (location_id,)).fetchone()
    restaurants = conn.execute('''
        SELECT r.*, AVG(rt.overall_rating) as avg_rating
        FROM restaurants r
        LEFT JOIN ratings rt ON r.id = rt.restaurant_id
        WHERE r.location_id = ?
        GROUP BY r.id
        ORDER BY r.name
    ''', (location_id,)).fetchall()
    conn.close()
    
    return render_template('restaurants.html', restaurants=restaurants, location=location)

@app.route('/restaurant/<int:restaurant_id>')
def restaurant_details(restaurant_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    conn = get_db_connection()
    restaurant = conn.execute('SELECT * FROM restaurants WHERE id = ?', (restaurant_id,)).fetchone()
    tables = conn.execute('SELECT * FROM restaurant_tables WHERE restaurant_id = ? AND is_available = 1', 
                         (restaurant_id,)).fetchall()
    special_offers = conn.execute('SELECT * FROM special_offers WHERE restaurant_id = ? AND is_active = 1', 
                                 (restaurant_id,)).fetchall()
    conn.close()
    
    return render_template('restaurant_details.html', restaurant=restaurant, tables=tables, special_offers=special_offers)

@app.route('/menu/<int:restaurant_id>')
def view_menu(restaurant_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    conn = get_db_connection()
    restaurant = conn.execute('SELECT * FROM restaurants WHERE id = ?', (restaurant_id,)).fetchone()
    
    # Filter menu items based on restaurant type
    if restaurant['is_veg_only']:
        menu_items = conn.execute('SELECT * FROM menu_items WHERE restaurant_id = ? AND is_veg = 1 ORDER BY category', 
                                 (restaurant_id,)).fetchall()
    else:
        menu_items = conn.execute('SELECT * FROM menu_items WHERE restaurant_id = ? ORDER BY category', 
                                 (restaurant_id,)).fetchall()
    
    conn.close()
    
    return render_template('menu.html', restaurant=restaurant, menu_items=menu_items)

@app.route('/book-table', methods=['POST'])
def book_table():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    restaurant_id = request.form['restaurant_id']
    table_id = request.form['table_id']
    booking_date = request.form['booking_date']
    booking_time = request.form['booking_time']
    party_size = request.form['party_size']
    
    conn = get_db_connection()
    
    # Check if table is still available
    table = conn.execute('SELECT * FROM restaurant_tables WHERE id = ? AND is_available = 1', 
                        (table_id,)).fetchone()
    
    if table:
        # Create booking
        conn.execute('''INSERT INTO bookings 
                       (user_id, restaurant_id, table_id, booking_date, booking_time, party_size) 
                       VALUES (?, ?, ?, ?, ?, ?)''',
                    (session['user_id'], restaurant_id, table_id, booking_date, booking_time, party_size))
        
        # Mark table as unavailable
        conn.execute('UPDATE restaurant_tables SET is_available = 0 WHERE id = ?', (table_id,))
        
        conn.commit()
        flash('Table booked successfully!')
    else:
        flash('Sorry, this table is no longer available.')
    
    conn.close()
    return redirect(url_for('restaurant_details', restaurant_id=restaurant_id))

@app.route('/rate-restaurant/<int:restaurant_id>', methods=['GET', 'POST'])
def rate_restaurant(restaurant_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        customer_service = int(request.form['customer_service'])
        food_quality = int(request.form['food_quality'])
        respect = int(request.form['respect'])
        review_text = request.form['review_text']
        overall_rating = (customer_service + food_quality + respect) / 3
        
        conn = get_db_connection()
        conn.execute('''INSERT INTO ratings 
                       (user_id, restaurant_id, customer_service, food_quality, respect, overall_rating, review_text) 
                       VALUES (?, ?, ?, ?, ?, ?, ?)''',
                    (session['user_id'], restaurant_id, customer_service, food_quality, respect, overall_rating, review_text))
        conn.commit()
        conn.close()
        
        flash('Rating submitted successfully!')
        return redirect(url_for('restaurant_details', restaurant_id=restaurant_id))
    
    conn = get_db_connection()
    restaurant = conn.execute('SELECT * FROM restaurants WHERE id = ?', (restaurant_id,)).fetchone()
    conn.close()
    
    return render_template('rate_restaurant.html', restaurant=restaurant)

@app.route('/admin-dashboard')
def admin_dashboard():
    if 'admin_restaurant_id' not in session:
        return redirect(url_for('admin_login'))
    
    conn = get_db_connection()
    restaurant_id = session['admin_restaurant_id']
    
    # Get bookings for this restaurant
    bookings = conn.execute('''
        SELECT b.*, u.username, rt.table_number 
        FROM bookings b
        JOIN users u ON b.user_id = u.id
        JOIN restaurant_tables rt ON b.table_id = rt.id
        WHERE b.restaurant_id = ?
        ORDER BY b.booking_date DESC, b.booking_time DESC
    ''', (restaurant_id,)).fetchall()
    
    # Get special offers
    special_offers = conn.execute('SELECT * FROM special_offers WHERE restaurant_id = ? ORDER BY created_at DESC', 
                                 (restaurant_id,)).fetchall()
    
    conn.close()
    
    return render_template('admin_dashboard.html', bookings=bookings, special_offers=special_offers)

@app.route('/admin-add-offer', methods=['GET', 'POST'])
def admin_add_offer():
    if 'admin_restaurant_id' not in session:
        return redirect(url_for('admin_login'))
    
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        discount_percentage = float(request.form['discount_percentage'])
        valid_from = request.form['valid_from']
        valid_to = request.form['valid_to']
        
        conn = get_db_connection()
        conn.execute('''INSERT INTO special_offers 
                       (restaurant_id, title, description, discount_percentage, valid_from, valid_to) 
                       VALUES (?, ?, ?, ?, ?, ?)''',
                    (session['admin_restaurant_id'], title, description, discount_percentage, valid_from, valid_to))
        conn.commit()
        conn.close()
        
        flash('Special offer added successfully!')
        return redirect(url_for('admin_dashboard'))
    
    return render_template('admin_add_offer.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

@app.route('/admin-logout')
def admin_logout():
    session.clear()
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    populate_sample_data()
    app.run(debug=True)
