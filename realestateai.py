import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import io
import os
import datetime
import uuid
import matplotlib.pyplot as plt
import seaborn as sns
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(
    page_title="DirectHome - No Agents, Just Properties",
    page_icon="🏠",
    layout="wide"
)

# Initialize session state variables
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if 'current_user' not in st.session_state:
    st.session_state.current_user = None
if 'properties' not in st.session_state:
    # Mock database of properties
    st.session_state.properties = pd.DataFrame({
        'id': ['prop1', 'prop2', 'prop3'],
        'title': ['Modern Condo in Downtown', 'Spacious Family Home', 'Renovated Townhouse'],
        'price': [450000, 750000, 550000],
        'address': ['123 Main St, Downtown, City', '456 Oak Ave, Suburb, City', '789 Pine St, Midtown, City'],
        'city': ['Downtown', 'Suburb', 'Midtown'],
        'state': ['NY', 'CA', 'TX'],
        'zip_code': ['10001', '90210', '75001'],
        'bedrooms': [2, 4, 3],
        'bathrooms': [2, 3, 2.5],
        'sqft': [1200, 2500, 1800],
        'property_type': ['Condo', 'House', 'Townhouse'],
        'year_built': [2010, 1995, 2005],
        'description': [
            'Beautiful modern condo with great views and amenities.',
            'Perfect family home with large backyard and updated kitchen.',
            'Recently renovated townhouse in a quiet neighborhood.'
        ],
        'features': [
            ['Garage', 'Central AC', 'Hardwood Floors'],
            ['Pool', 'Garage', 'Fireplace', 'Large Yard'],
            ['Renovated Kitchen', 'Hardwood Floors', 'Deck/Patio']
        ],
        'seller_id': ['user1', 'user2', 'user3'],
        'date_listed': ['2025-02-15', '2025-03-01', '2025-03-10'],
        'views': [120, 85, 45]
    })
if 'users' not in st.session_state:
    # Mock users database
    st.session_state.users = pd.DataFrame({
        'id': ['user1', 'user2', 'user3', 'user4'],
        'username': ['sarah_j', 'michael_t', 'lisa_m', 'john_d'],
        'email': ['sarah@example.com', 'michael@example.com', 'lisa@example.com', 'john@example.com'],
        'password': ['pass123', 'pass123', 'pass123', 'pass123'],  # In a real app, these would be hashed
        'name': ['Sarah Johnson', 'Michael Thomas', 'Lisa Miller', 'John Davis']
    })
if 'messages' not in st.session_state:
    # Mock messages database
    st.session_state.messages = pd.DataFrame({
        'id': ['msg1', 'msg2', 'msg3'],
        'property_id': ['prop1', 'prop1', 'prop2'],
        'sender_id': ['user4', 'user1', 'user4'],
        'receiver_id': ['user1', 'user4', 'user2'],
        'message': [
            'I\'m interested in your downtown condo. Is it still available?',
            'Yes, it\'s still available. When would you like to see it?',
            'How old is the HVAC system in your family home?'
        ],
        'timestamp': ['2025-03-18 14:30:00', '2025-03-18 15:45:00', '2025-03-19 10:15:00'],
        'read': [True, False, True]
    })
if 'uploaded_images' not in st.session_state:
    st.session_state.uploaded_images = {}

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1E3A8A;
        margin-bottom: 0;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #6B7280;
        margin-top: 0;
    }
    .card {
        border: 1px solid #E5E7EB;
        border-radius: 0.5rem;
        padding: 1rem;
        margin-bottom: 1rem;
        background-color: white;
    }
    .price {
        font-size: 1.5rem;
        font-weight: bold;
        color: #1E3A8A;
    }
    .address {
        color: #4B5563;
        margin-bottom: 0.5rem;
    }
    .specs {
        color: #6B7280;
        font-size: 0.9rem;
    }
    .feature-tag {
        background-color: #EFF6FF;
        color: #1E40AF;
        padding: 0.2rem 0.5rem;
        border-radius: 0.25rem;
        font-size: 0.8rem;
        margin-right: 0.25rem;
        margin-bottom: 0.25rem;
        display: inline-block;
    }
    .section-header {
        font-size: 1.5rem;
        font-weight: bold;
        color: #1E3A8A;
        margin-top: 2rem;
        margin-bottom: 1rem;
    }
    .step-box {
        background-color: #F3F4F6;
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center;
    }
    .step-icon {
        font-size: 2rem;
        margin-bottom: 0.5rem;
    }
    .testimonial {
        font-style: italic;
        padding: 1rem;
        background-color: #F9FAFB;
        border-left: 4px solid #1E3A8A;
        margin-bottom: 1rem;
    }
    .progress-step {
        background-color: #E5E7EB;
        color: #4B5563;
        padding: 0.5rem 1rem;
        border-radius: 9999px;
        font-size: 0.9rem;
        margin-right: 0.5rem;
        margin-bottom: 0.5rem;
        display: inline-block;
    }
    .progress-step.active {
        background-color: #1E3A8A;
        color: white;
    }
    .heatmap-cell {
        text-align: center;
        padding: 0.5rem;
        color: white;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Authentication functions
def login(username, password):
    users = st.session_state.users
    user = users[(users['username'] == username) & (users['password'] == password)]
    if not user.empty:
        st.session_state.logged_in = True
        st.session_state.current_user = user.iloc[0]['id']
        return True
    return False

def register(username, email, password, name):
    users = st.session_state.users
    if any(users['username'] == username) or any(users['email'] == email):
        return False
    
    new_id = f"user{len(users) + 1}"
    new_user = pd.DataFrame({
        'id': [new_id],
        'username': [username],
        'email': [email],
        'password': [password],
        'name': [name]
    })
    
    st.session_state.users = pd.concat([users, new_user], ignore_index=True)
    st.session_state.logged_in = True
    st.session_state.current_user = new_id
    return True

def logout():
    st.session_state.logged_in = False
    st.session_state.current_user = None

# AI pricing model function
def estimate_property_price(property_data):
    """
    Simulated AI pricing model that estimates property value based on various factors
    """
    # Base price by property type
    base_prices = {
        'House': 300000,
        'Condo': 200000,
        'Townhouse': 250000,
        'Apartment': 150000,
        'Land': 100000
    }
    
    # Get base price based on property type, default to average if not found
    base_price = base_prices.get(property_data.get('property_type', ''), 250000)
    
    # Adjust for property attributes
    bedroom_value = int(property_data.get('bedrooms', 3)) * 50000
    bathroom_value = float(property_data.get('bathrooms', 2)) * 25000
    sqft_value = int(property_data.get('sqft', 1500)) * 150
    
    # Adjust for features
    features = property_data.get('features', [])
    feature_value = len(features) * 5000
    
    # Adjust for location (simplified)
    location_multipliers = {
        'NY': 1.5,
        'CA': 1.4,
        'TX': 1.1,
        'FL': 1.2
    }
    location_multiplier = location_multipliers.get(property_data.get('state', ''), 1.0)
    
    # Calculate estimated price
    estimated_price = (base_price + bedroom_value + bathroom_value + sqft_value + feature_value) * location_multiplier
    
    # Add some randomness to simulate market variations (±5%)
    randomness = np.random.uniform(0.95, 1.05)
    final_estimate = estimated_price * randomness
    
    # Generate price range
    low_estimate = final_estimate * 0.95
    high_estimate = final_estimate * 1.05
    
    # Generate comparable properties
    comps = generate_comparable_properties(property_data, final_estimate)
    
    return {
        'estimate': int(final_estimate),
        'range': {
            'low': int(low_estimate),
            'high': int(high_estimate)
        },
        'comparables': comps
    }

def generate_comparable_properties(property_data, estimated_price):
    """Generate list of comparable properties for AI price estimator"""
    comps = []
    
    # Generate 3 comparable properties with slight variations
    for i in range(3):
        price_variation = np.random.uniform(0.93, 1.07)
        bedroom_variation = np.random.randint(-1, 2)
        bathroom_variation = np.random.choice([-0.5, 0, 0.5])
        sqft_variation = np.random.randint(-200, 201)
        days_ago = np.random.randint(15, 90)
        
        comp = {
            'address': f"{np.random.randint(100, 999)} {np.random.choice(['Oak', 'Pine', 'Maple', 'Cedar', 'Elm'])} {np.random.choice(['St', 'Ave', 'Blvd', 'Dr'])}",
            'price': int(estimated_price * price_variation),
            'bedrooms': max(1, int(property_data.get('bedrooms', 3)) + bedroom_variation),
            'bathrooms': max(1, float(property_data.get('bathrooms', 2)) + bathroom_variation),
            'sqft': max(500, int(property_data.get('sqft', 1500)) + sqft_variation),
            'days_ago': days_ago
        }
        comps.append(comp)
    
    return comps

# Navigation
def show_navigation():
    # Check if user is logged in
    if st.session_state.logged_in:
        # Get user information
        user_id = st.session_state.current_user
        user_info = st.session_state.users[st.session_state.users['id'] == user_id].iloc[0]
        
        # Display user info and logout button in sidebar
        with st.sidebar:
            st.write(f"Welcome, {user_info['name']}!")
            if st.button("Log Out"):
                logout()
                st.experimental_rerun()
    
    # Main navigation
    selected = option_menu(
        menu_title=None,
        options=["Home", "Buy", "Sell", "My Account", "Messages"],
        icons=["house", "search", "upload", "person", "envelope"],
        menu_icon="cast",
        default_index=0,
        orientation="horizontal",
    )
    
    if selected == "Home":
        show_home_page()
    elif selected == "Buy":
        show_buy_page()
    elif selected == "Sell":
        if not st.session_state.logged_in:
            show_login_page(redirect="sell")
        else:
            show_sell_page()
    elif selected == "My Account":
        if not st.session_state.logged_in:
            show_login_page(redirect="account")
        else:
            show_account_page()
    elif selected == "Messages":
        if not st.session_state.logged_in:
            show_login_page(redirect="messages")
        else:
            show_messages_page()

# Page functions
def show_home_page():
    # Hero section
    st.markdown('<h1 class="main-header">Find Your Dream Home or Sell Directly</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">No agents. No commissions. Just properties and people.</p>', unsafe_allow_html=True)
    
    # Search bar
    col1, col2, col3, col4 = st.columns([2, 1, 1, 1])
    with col1:
        location = st.text_input("Location", placeholder="City, State, or ZIP")
    with col2:
        price_range = st.selectbox("Price Range", ["Any", "Under $300k", "$300k-$500k", "$500k-$750k", "$750k-$1M", "$1M+"])
    with col3:
        beds = st.selectbox("Beds", ["Any", "1+", "2+", "3+", "4+", "5+"])
    with col4:
        property_type = st.selectbox("Property Type", ["Any", "House", "Condo", "Townhouse", "Apartment", "Land"])
    
    if st.button("Search Properties"):
        st.session_state.search_params = {
            "location": location,
            "price_range": price_range,
            "beds": beds,
            "property_type": property_type
        }
        # In a real app, this would filter properties and navigate to results
        st.info("In a real app, this would display search results based on your criteria.")
    
    # Featured properties
    st.markdown('<h2 class="section-header">Featured Properties</h2>', unsafe_allow_html=True)
    
    # Display properties in a grid of 3
    props = st.session_state.properties.head(3)
    cols = st.columns(3)
    
    for i, (_, prop) in enumerate(props.iterrows()):
        with cols[i]:
            st.markdown(f"""
            <div class="card">
                <img src="https://placekitten.com/400/250?image={i+1}" style="width: 100%; border-radius: 0.25rem;">
                <div style="padding: 0.5rem 0;">
                    <div class="price">${prop['price']:,}</div>
                    <div class="address">{prop['address']}</div>
                    <div class="specs">{prop['bedrooms']} bd | {prop['bathrooms']} ba | {prop['sqft']:,} sqft | {prop['property_type']}</div>
                    <div style="margin-top: 0.5rem;">
                        {"".join([f'<span class="feature-tag">{feature}</span>' for feature in prop['features'][:3]])}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            if st.button("View Details", key=f"view_prop_{prop['id']}"):
                st.session_state.selected_property = prop['id']
                st.experimental_rerun()  # In a real app, this would navigate to property details
    
    # How it works section
    st.markdown('<h2 class="section-header">How It Works</h2>', unsafe_allow_html=True)
    
    cols = st.columns(4)
    
    with cols[0]:
        st.markdown("""
        <div class="step-box">
            <div class="step-icon">📸</div>
            <h3>Upload Photos</h3>
            <p>Take photos of your property and upload them to create your listing.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[1]:
        st.markdown("""
        <div class="step-box">
            <div class="step-icon">🤖</div>
            <h3>Get AI Price Estimate</h3>
            <p>Our AI algorithm analyzes your property and suggests a competitive price.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[2]:
        st.markdown("""
        <div class="step-box">
            <div class="step-icon">📝</div>
            <h3>List Your Property</h3>
            <p>Create your listing with all details and set your price.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[3]:
        st.markdown("""
        <div class="step-box">
            <div class="step-icon">🤝</div>
            <h3>Connect with Buyers</h3>
            <p>Receive inquiries directly from interested buyers.</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Testimonials section
    st.markdown('<h2 class="section-header">Success Stories</h2>', unsafe_allow_html=True)
    
    cols = st.columns(3)
    
    with cols[0]:
        st.markdown("""
        <div class="testimonial">
            <p>"I sold my condo in just 3 weeks and saved over $15,000 in commissions!"</p>
            <div>- Sarah J.</div>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[1]:
        st.markdown("""
        <div class="testimonial">
            <p>"The AI pricing tool was spot on. I got multiple offers within my asking price range."</p>
            <div>- Michael T.</div>
        </div>
        """, unsafe_allow_html=True)
    
    with cols[2]:
        st.markdown("""
        <div class="testimonial">
            <p>"Bought my first home directly from the owner. The process was surprisingly smooth."</p>
            <div>- Lisa M.</div>
        </div>
        """, unsafe_allow_html=True)

def show_buy_page():
    st.markdown('<h1 class="main-header">Find Your Perfect Property</h1>', unsafe_allow_html=True)
    
    # Filter options (top sidebar)
    with st.expander("Filter Options", expanded=True):
        col1, col2 = st.columns(2)
        
        with col1:
            location = st.text_input("Location", placeholder="City, State, or ZIP")
            price_min = st.number_input("Min Price", min_value=0, max_value=10000000, value=0, step=50000)
            price_max = st.number_input("Max Price", min_value=0, max_value=10000000, value=1000000, step=50000)
            beds = st.select_slider("Minimum Bedrooms", options=["Any", "1+", "2+", "3+", "4+", "5+"])
        
        with col2:
            baths = st.select_slider("Minimum Bathrooms", options=["Any", "1+", "1.5+", "2+", "2.5+", "3+", "4+"])
            property_type = st.multiselect("Property Type", ["House", "Condo", "Townhouse", "Apartment", "Land"], default=[])
            features = st.multiselect("Features", [
                "Garage", "Pool", "Fireplace", "Central AC", "Basement", 
                "Renovated Kitchen", "Hardwood Floors", "Smart Home", "Deck/Patio"
            ], default=[])
        
        apply_button = st.button("Apply Filters")
    
    # Sort options
    col1, col2 = st.columns([3, 1])
    with col1:
        st.write(f"{len(st.session_state.properties)} properties found")
    with col2:
        sort_by = st.selectbox("Sort by", ["Newest", "Price (High to Low)", "Price (Low to High)"])
    
    # Property listings
    properties = st.session_state.properties  # In a real app, this would be filtered
    
    for _, prop in properties.iterrows():
        col1, col2 = st.columns([1, 2])
        
        with col1:
            st.image("https://placekitten.com/400/300?image="+str(np.random.randint(1, 10)), use_column_width=True)
        
        with col2:
            st.markdown(f"""
            <div style="padding: 0 1rem;">
                <div class="price">${prop['price']:,}</div>
                <div class="address">{prop['address']}</div>
                <div class="specs">{prop['bedrooms']} bd | {prop['bathrooms']} ba | {prop['sqft']:,} sqft | {prop['property_type']}</div>
                <div style="margin-top: 0.5rem;">
                    {"".join([f'<span class="feature-tag">{feature}</span>' for feature in prop['features']])}
                </div>
                <p>{prop['description'][:150]}...</p>
            </div>
            """, unsafe_allow_html=True)
            
            view_col, contact_col = st.columns(2)
            with view_col:
                if st.button("View Details", key=f"view_{prop['id']}"):
                    st.session_state.selected_property = prop['id']
                    # In a real app, this would navigate to property details page
                    st.info(f"Viewing {prop['title']} details")
            
            with contact_col:
                if st.button("Contact Seller", key=f"contact_{prop['id']}"):
                    if not st.session_state.logged_in:
                        st.warning("Please log in to contact the seller")
                    else:
                        # In a real app, this would open a message form
                        st.info(f"Contacting seller about {prop['title']}")
        
        st.markdown("<hr>", unsafe_allow_html=True)

def show_sell_page():
    st.markdown('<h1 class="main-header">Sell Your Property</h1>', unsafe_allow_html=True)
    
    # Initialize selling process step if not exists
    if 'sell_step' not in st.session_state:
        st.session_state.sell_step = 1
    if 'property_data' not in st.session_state:
        st.session_state.property_data = {
            'title': '',
            'description': '',
            'price': '',
            'address': '',
            'city': '',
            'state': '',
            'zip_code': '',
            'property_type': '',
            'bedrooms': '',
            'bathrooms': '',
            'sqft': '',
            'year_built': '',
            'features': []
        }
    if 'ai_estimate' not in st.session_state:
        st.session_state.ai_estimate = None
    
    # Progress tracker
    steps = ["Property Details", "Upload Photos", "AI Price Estimate", "Review & List"]
    st.markdown(
        "".join([f'<span class="progress-step {"active" if i+1 <= st.session_state.sell_step else ""}">{i+1}. {step}</span>' for i, step in enumerate(steps)]),
        unsafe_allow_html=True
    )
    
    # Step 1: Property Details
    if st.session_state.sell_step == 1:
        st.subheader("Property Details")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.session_state.property_data['title'] = st.text_input(
                "Property Title",
                value=st.session_state.property_data['title'],
                placeholder="E.g., Beautiful Family Home with Pool"
            )
            
            st.session_state.property_data['address'] = st.text_input(
                "Street Address",
                value=st.session_state.property_data['address'],
                placeholder="123 Main St"
            )
            
            city_col, state_col, zip_col = st.columns([2, 1, 1])
            with city_col:
                st.session_state.property_data['city'] = st.text_input(
                    "City",
                    value=st.session_state.property_data['city']
                )
            with state_col:
                st.session_state.property_data['state'] = st.text_input(
                    "State",
                    value=st.session_state.property_data['state'],
                    max_chars=2
                )
            with zip_col:
                st.session_state.property_data['zip_code'] = st.text_input(
                    "ZIP Code",
                    value=st.session_state.property_data['zip_code']
                )
            
            st.session_state.property_data['property_type'] = st.selectbox(
                "Property Type",
                options=["", "House", "Condo", "Townhouse", "Apartment", "Land"],
                index=0 if st.session_state.property_data['property_type'] == '' else 
                    ["", "House", "Condo", "Townhouse", "Apartment", "Land"].index(st.session_state.property_data['property_type'])
            )
        
        with col2:
            bed_bath_cols = st.columns(2)
            with bed_bath_cols[0]:
                st.session_state.property_data['bedrooms'] = st.number_input(
                    "Bedrooms",
                    min_value=0,
                    max_value=20,
                    value=int(st.session_state.property_data['bedrooms']) if st.session_state.property_data['bedrooms'] != '' else 0
                )
            
            with bed_bath_cols[1]:
                st.session_state.property_data['bathrooms'] = st.number_input(
                    "Bathrooms",
                    min_value=0.0,
                    max_value=20.0,
                    step=0.5,
                    value=float(st.session_state.property_data['bathrooms']) if st.session_state.property_data['bathrooms'] != '' else 0.0
                )
            
            st.session_state.property_data['sqft'] = st.number_input(
                "Square Footage",
                min_value=0,
                max_value=100000,
                value=int(st.session_state.property_data['sqft']) if st.session_state.property_data['sqft'] != '' else 0
            )
            
            st.session_state.property_data['year_built'] = st.number_input(
                "Year Built",
                min_value=1800,
                max_value=2025,
                value=int(st.session_state.property_data['year_built']) if st.session_state.property_data['year_built'] != '' else 2000
            )
            
            st.markdown("<label>Features (select all that apply)</label>", unsafe_allow_html=True)
            feature_options = [
                "Garage", "Pool", "Fireplace", "Central AC", "Basement", 
                "Renovated Kitchen", "Hardwood Floors", "Smart Home", 
                "Solar Panels", "Large Yard", "Deck/Patio", "Waterfront"
            ]
            
            # Create a 3-column layout for features
            feature_cols = st.columns(3)
            col_idx = 0
            
            for feature in feature_options:
                with feature_cols[col_idx]:
                    is_selected = feature in st.session_state.property_data['features']
                    if st.checkbox(feature, value=is_selected, key=f"feature_{feature}"):
                        if feature not in st.session_state.property_data['features']:
                            st.session_state.property_data['features'].append(feature)
                    else:
                        if feature in st.session_state.property_data['features']:
                            st.session_state.property_data['features'].remove(feature)
                
                col_idx = (col_idx + 1) % 3
        
        # Description field spans both columns
        st.session_state.property_data['description'] = st.text_area(
            "Property Description",
            value=st.session_state.property_data['description'],
            height=150,
            placeholder="Describe your property in detail. Highlight special features, recent renovations, and what makes it special."
        )
        
        # Navigation buttons
        next_col, _ = st.columns([1, 5])
        with next_col:
            if st.button("Next: Upload Photos"):
                # Validate inputs (basic validation)
                required_fields = ['title', 'address', 'city', 'state', 'zip_code', 'property_type', 'description']
                missing_fields = [field for field in required_fields if st.session_state.property_data[field] == '']
                
                if missing_fields:
                    st.error(f"Please fill in all required fields: {', '.join(missing_fields)}")
                else:
                    st.session_state.sell_step = 2
                    st.experimental_rerun()
    
    # Step 2: Upload Photos
    elif st.session_state.sell_step == 2:
        st.subheader("Upload Property Photos")
        st.write("High-quality photos increase interest in your property. Upload at least 5 photos.")
        
        # Image upload tips
        with st.expander("Tips for Great Property Photos", expanded=False):
            st.markdown("""
            - Use natural lighting when possible
            - Take photos during the day
            - Include all main rooms and exterior views
            - Keep the space clean and decluttered
            - Capture your property's best features
            """)
        
        # Image uploader
        uploaded_files = st.file_uploader(
            "Upload Property Images",
            type=["jpg", "jpeg",
