# 🍽️ Restaurant Table Booking System

A comprehensive web application for restaurant table booking built with Flask, HTML, CSS, and SQLite3.

## 🌟 Features

### User Features
- **User Registration & Login**: Secure user authentication system
- **Location Selection**: Choose from Tamil Nadu cities (Karur, Chennai, Madurai, Salem, etc.)
- **Restaurant Discovery**: Browse restaurants by location with ratings and cuisine types
- **Table Booking**: Select available tables with date, time, and party size
- **Menu Viewing**: View restaurant menus with veg/non-veg filtering
- **Rating System**: Rate restaurants on customer service, food quality, and respect
- **Special Offers**: View restaurant-specific special offers and discounts

### Admin Features
- **Admin Dashboard**: Restaurant-specific admin access
- **Booking Management**: View all bookings for your restaurant
- **Special Offers**: Create and manage special offers for customers
- **Table Management**: Monitor table availability and bookings

## 🛠️ Technologies Used

- **Backend**: Flask (Python web framework)
- **Database**: SQLite3
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with responsive design
- **Icons**: Font Awesome icons

## 📋 Installation & Setup

1. **Clone or download** this project
2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
3. **Setup database** (automatic on first run):
   ```bash
   python setup_database.py
   ```
4. **Run the application**:
   ```bash
   python run.py
   ```
5. **Open browser** to `http://localhost:5000`

## 👥 Login Information

### Sample User Accounts
- **Usernames**: john_doe, jane_smith, ravi_kumar, priya_singh
- **Password**: password123
- Or register a new account

### Admin Access
- **Username**: Restaurant name (exact match)
  - Valluvar Restaurant
  - Thalapakatti Hotel
  - Saravana Bhavan
  - Buhari Hotel
  - Anjappar
  - Meenakshi Bhavan
- **Password**: admin123 (same for all restaurants)

## 🗺️ Available Locations & Restaurants

### Karur
- **Valluvar Restaurant** (Pure Vegetarian) - South Indian cuisine
- **Thalapakatti Hotel** (Multi-cuisine) - Famous for Dindigul biryani

### Chennai
- **Saravana Bhavan** (Pure Vegetarian) - Popular chain restaurant
- **Buhari Hotel** (Multi-cuisine) - Heritage restaurant since 1951

### Madurai
- **Anjappar** (Multi-cuisine) - Authentic Chettinad cuisine
- **Meenakshi Bhavan** (Pure Vegetarian) - Traditional temple city flavors

## 🎯 User Journey

1. **Home Page**: Choose between User Login/Register or Admin Login
2. **Registration**: New users create account with username, password, email, phone
3. **Login**: Existing users sign in with credentials
4. **Location Selection**: Choose from Tamil Nadu cities
5. **Restaurant Browsing**: View restaurants in selected location with ratings
6. **Restaurant Details**: See restaurant info, special offers, and available tables
7. **Menu Viewing**: Browse menu items (filtered by restaurant type - veg/non-veg)
8. **Table Booking**: Select table, date, time, and party size
9. **Rating**: Rate restaurant experience on multiple criteria

## 👨‍💼 Admin Journey

1. **Admin Login**: Use restaurant name as username, admin123 as password
2. **Dashboard**: View booking statistics and recent bookings
3. **Booking Management**: See all customer bookings for your restaurant
4. **Special Offers**: Create and manage promotional offers
5. **Customer Insights**: Monitor ratings and reviews

## 📊 Database Schema

- **users**: User account information
- **locations**: Tamil Nadu cities
- **restaurants**: Restaurant details and cuisine types
- **restaurant_tables**: Table information for each restaurant
- **bookings**: Customer booking records
- **menu_items**: Restaurant menu items with veg/non-veg classification
- **ratings**: Customer ratings and reviews
- **special_offers**: Admin-created promotional offers

## 🔧 Key Features Implementation

### Smart Menu Filtering
- Pure vegetarian restaurants (like Valluvar Restaurant) only show vegetarian items
- Multi-cuisine restaurants show both veg and non-veg items with clear indicators

### Table Availability
- Real-time table availability tracking
- Tables become unavailable once booked
- Visual table selection interface

### Rating System
- Multi-criteria rating: Customer Service, Food Quality, Respect
- Overall rating calculation
- Restaurant-wise rating aggregation

### Admin Security
- Restaurant-specific admin access
- Each admin can only see their restaurant's data
- Simple authentication with restaurant name + default password

## 🎨 Design Features

- **Responsive Design**: Works on desktop, tablet, and mobile
- **Modern UI**: Clean, professional interface with gradients and shadows
- **Interactive Elements**: Hover effects, animations, and smooth transitions
- **Icon Integration**: Font Awesome icons for better UX
- **Color Coding**: Green for vegetarian, red for non-vegetarian items
- **Visual Feedback**: Success/error messages and loading states

## 🚀 Quick Start

```bash
# Navigate to project directory
cd "Restaurant Booking System"

# Install dependencies
pip install -r requirements.txt

# Run the application
python run.py
```

Open `http://localhost:5000` in your browser and start exploring!

## 📱 Mobile Responsive

The application is fully responsive and works seamlessly on:
- Desktop computers
- Tablets
- Mobile phones

## 🔐 Security Features

- Session-based authentication
- Input validation and sanitization
- SQL injection prevention with parameterized queries
- User authorization checks for all protected routes

## 🎯 Future Enhancements

- Payment integration
- Email notifications for bookings
- Advanced search and filtering
- Customer loyalty programs
- Restaurant analytics dashboard
- Mobile app development

---

**Developed with ❤️ for Tamil Nadu's vibrant food culture**
