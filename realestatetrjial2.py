import streamlit as st

# Page config
st.set_page_config(page_title="HomeDirect", layout="wide")

# Sample listings data
listings = [
    {
        "image": "https://via.placeholder.com/600x400",
        "price": 350000,
        "title": "Beautiful Family Home",
        "location": "Portland, OR",
        "bedrooms": 3,
        "bathrooms": 2,
        "sqft": 1800,
    },
    {
        "image": "https://via.placeholder.com/600x400",
        "price": 475000,
        "title": "Modern Condo Downtown",
        "location": "Seattle, WA",
        "bedrooms": 2,
        "bathrooms": 2,
        "sqft": 1300,
    },
    {
        "image": "https://via.placeholder.com/600x400",
        "price": 250000,
        "title": "Cozy Country Cottage",
        "location": "Boise, ID",
        "bedrooms": 2,
        "bathrooms": 1,
        "sqft": 900,
    },
]

# --- Hero Section ---
st.markdown("## 🏡 Buy and Sell Properties Directly")
st.write("Cut out the middleman and save thousands on agent fees. Connect directly with buyers and sellers in your area.")

with st.form("search_form"):
    col1, col2, col3 = st.columns(3)
    with col1:
        location = st.text_input("Location / Zip / Address")
    with col2:
        property_type = st.selectbox("Property Type", ["", "House", "Apartment", "Condo", "Land"])
    with col3:
        price_range = st.selectbox("Price Range", ["", "Under $100k", "$100k - $200k", "$200k - $300k", "$300k - $500k", "$500k+"])
    st.form_submit_button("Search")

# --- Why Choose Us ---
st.markdown("### 🌟 Why Choose HomeDirect?")
st.write("Our platform is designed to simplify the real estate process and save you money.")

cols = st.columns(3)
with cols[0]:
    st.markdown("#### 💰 Save on Commissions")
    st.write("Avoid agent fees (5-6% of your property value). Keep more money in your pocket.")
with cols[1]:
    st.markdown("#### 🤝 Direct Communication")
    st.write("Connect directly with buyers or sellers without a middleman.")
with cols[2]:
    st.markdown("#### 📱 Easy-to-Use Platform")
    st.write("Our intuitive interface makes listing or finding properties simple and stress-free.")

# --- Featured Listings ---
st.markdown("### 🏠 Featured Listings")
st.write("Browse our latest properties for sale directly from owners.")

for listing in listings:
    st.image(listing["image"], width=600)
    st.markdown(f"**{listing['title']}**  \n📍 {listing['location']}")
    st.write(f"💵 ${listing['price']:,} | 🛏 {listing['bedrooms']} | 🛁 {listing['bathrooms']} | 📐 {listing['sqft']} sq ft")
    st.markdown("---")

# --- How It Works ---
st.markdown("### 🛠️ How It Works")
steps = [
    ("Create Your Account", "Sign up for free and verify your identity to get started."),
    ("List Your Property", "Upload photos, add detailed descriptions, and set your price."),
    ("Connect With Buyers/Sellers", "Message directly to arrange viewings and negotiations."),
    ("Close The Deal", "Use our resources to safely complete your transaction."),
]
for step in steps:
    st.markdown(f"#### {step[0]}")
    st.write(step[1])

# --- Testimonials ---
st.markdown("### 💬 What Our Users Say")
testimonials = [
    ("Sarah Johnson", "Home Seller", "I saved over $15,000 by selling my home on HomeDirect instead of using a traditional agent."),
    ("Michael Chen", "Home Buyer", "As a first-time buyer, I appreciated direct communication with the seller."),
    ("David Rodriguez", "Home Seller", "The dashboard makes it easy to manage listings. I’ve sold two properties here."),
]
for name, role, quote in testimonials:
    st.markdown(f"> *\"{quote}\"*  \n— **{name}**, *{role}*")

# --- Call to Action ---
st.markdown("## 🚀 Ready to Get Started?")
st.write("Join thousands of users who have bought and sold properties without agent fees.")

col1, col2 = st.columns(2)
with col1:
    if st.button("Sign Up Now"):
        st.info("Redirecting to signup page... (add link)")
with col2:
    if st.button("Browse Listings"):
        st.info("Redirecting to listings page... (add link)")
