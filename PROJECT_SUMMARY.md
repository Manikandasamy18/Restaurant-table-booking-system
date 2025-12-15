# 🍽️ Restaurant Table Booking System - Complete Project

## 📁 Project Structure
```
Restaurant Booking System/
├── app.py                     # Main Flask application
├── run.py                     # Application startup script
├── setup_database.py          # Database initialization with sample data
├── test_app.py               # Test suite for verification
├── requirements.txt          # Python dependencies
├── README.md                 # Comprehensive documentation
├── restaurant_booking.db     # SQLite database (created automatically)
├── templates/                # HTML templates
│   ├── base.html            # Base template with navigation
│   ├── index.html           # Home page
│   ├── login.html           # User login page
│   ├── register.html        # User registration page
│   ├── admin_login.html     # Admin login page
│   ├── select_location.html # Location selection page
│   ├── restaurants.html     # Restaurant listing page
│   ├── restaurant_details.html # Restaurant details & booking
│   ├── menu.html            # Menu display page
│   ├── rate_restaurant.html # Rating submission page
│   ├── admin_dashboard.html # Admin dashboard
│   └── admin_add_offer.html # Admin add special offer page
└── static/
    └── css/
        └── style.css        # Complete CSS styling
```

## ✅ Implemented Features

### 🔐 Authentication System
- [x] User registration with username, email, phone
- [x] User login with session management
- [x] Admin login using restaurant name + admin123 password
- [x] Session-based authorization
- [x] Logout functionality for both users and admins

### 📍 Location & Restaurant Management
- [x] Tamil Nadu cities: Karur, Chennai, Madurai, Salem, Dindigul, Coimbatore, Trichy, Erode
- [x] Location-based restaurant filtering
- [x] Restaurant details with cuisine type and description
- [x] Vegetarian/Non-vegetarian restaurant classification

### 🍽️ Restaurant Features
- [x] **Valluvar Restaurant** (Karur) - Pure vegetarian, South Indian
- [x] **Thalapakatti Hotel** (Karur) - Multi-cuisine, famous for biryani
- [x] **Saravana Bhavan** (Chennai) - Pure vegetarian chain
- [x] **Buhari Hotel** (Chennai) - Multi-cuisine heritage restaurant
- [x] **Anjappar** (Madurai) - Chettinad cuisine
- [x] **Meenakshi Bhavan** (Madurai) - Traditional vegetarian

### 📋 Menu System
- [x] Restaurant-specific menus with categories (Breakfast, Lunch, Main Course, Starters, Beverages, Desserts)
- [x] Veg/Non-veg item classification with visual indicators
- [x] Smart filtering: Pure veg restaurants only show veg items
- [x] Price display and item descriptions
- [x] Menu categorization with icons

### 🪑 Table Booking System
- [x] Multiple tables per restaurant (10 tables each with varying capacities)
- [x] Visual table selection interface
- [x] Date and time selection
- [x] Party size specification
- [x] Real-time table availability tracking
- [x] Booking confirmation and status management

### ⭐ Rating System
- [x] Multi-criteria rating: Customer Service, Food Quality, Respect
- [x] 5-star rating interface with interactive stars
- [x] Overall rating calculation
- [x] Optional text reviews
- [x] Restaurant rating aggregation and display

### 🎉 Special Offers
- [x] Admin-created promotional offers
- [x] Discount percentage and validity period
- [x] Restaurant-specific offer display
- [x] Offer management interface for admins

### 👨‍💼 Admin Dashboard
- [x] Restaurant-specific admin access
- [x] Booking statistics and recent bookings table
- [x] Special offers management
- [x] Admin can only see their restaurant's data
- [x] Quick action cards and analytics

### 🎨 Design & UI
- [x] Modern responsive design with CSS Grid and Flexbox
- [x] Beautiful gradient backgrounds and card layouts
- [x] Font Awesome icons throughout the interface
- [x] Smooth animations and hover effects
- [x] Mobile-responsive design
- [x] Color-coded veg/non-veg indicators
- [x] Professional admin dashboard design

## 🗄️ Database Schema (8 Tables)

1. **users** - User account information
2. **locations** - Tamil Nadu cities
3. **restaurants** - Restaurant details, cuisine type, veg classification
4. **restaurant_tables** - Table numbers, capacity, availability
5. **bookings** - Customer reservations with date/time
6. **menu_items** - Restaurant menus with veg/non-veg classification
7. **ratings** - Customer ratings on multiple criteria
8. **special_offers** - Admin-created promotional offers

## 🔧 Key Functionalities

### User Flow
1. **Registration/Login** → Location Selection → Restaurant Browsing → Table Booking
2. **Menu Viewing** with smart veg/non-veg filtering
3. **Rating Submission** with multi-criteria evaluation
4. **Special Offers** viewing for selected restaurants

### Admin Flow
1. **Admin Login** (restaurant name + admin123) → Dashboard Overview
2. **Booking Management** - view all customer bookings
3. **Special Offers** - create and manage promotional campaigns
4. **Restaurant Analytics** - booking statistics and performance

### Smart Features
- **Veg Restaurant Logic**: Valluvar Restaurant (pure veg) only shows vegetarian menu items
- **Multi-cuisine Logic**: Thalapakatti Hotel shows both veg and non-veg items with clear indicators
- **Table Availability**: Real-time tracking, booked tables become unavailable
- **Admin Security**: Each admin only sees their own restaurant's data

## 🎯 Sample Data

### Sample Users (Username: Password)
- john_doe: password123
- jane_smith: password123
- ravi_kumar: password123
- priya_singh: password123

### Admin Access (Restaurant Name: Password)
- Valluvar Restaurant: admin123
- Thalapakatti Hotel: admin123
- Saravana Bhavan: admin123
- Buhari Hotel: admin123
- Anjappar: admin123
- Meenakshi Bhavan: admin123

## 🚀 Getting Started

1. **Install dependencies**: `pip install -r requirements.txt`
2. **Setup database**: `python setup_database.py`
3. **Run application**: `python run.py`
4. **Open browser**: `http://localhost:5000`

## 📊 Technical Highlights

- **Flask Framework**: Clean route structure with session management
- **SQLite Database**: Efficiently designed schema with foreign key relationships
- **Responsive CSS**: Modern grid-based layout with animations
- **Security**: Parameterized queries, session-based auth, input validation
- **User Experience**: Intuitive interface with visual feedback and error handling

## 🎨 Design Elements

- **Color Scheme**: Purple/blue gradients with professional styling
- **Typography**: Clean, readable fonts with proper hierarchy
- **Icons**: Contextual Font Awesome icons for better UX
- **Animations**: Smooth transitions and hover effects
- **Mobile-First**: Responsive design that works on all devices

---

**Status: ✅ COMPLETE - Ready for production use!**
