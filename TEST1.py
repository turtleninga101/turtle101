import os
import streamlit as st
import pandas as pd
from datetime import date

LISTINGS_CSV = "data/listings.csv"
USERS_CSV = "data/users.csv"

def init_data_files():
    """Initialize CSV files if they do not exist."""
    if not os.path.exists("data"):
        os.mkdir("data")
    if not os.path.exists(LISTINGS_CSV):
        df_listings = pd.DataFrame(columns=[
            "listing_id", "owner_email", "title", "address", "description",
            "price", "listed_date", "paid_listing_fee", "sold", "paid_selling_fee"
        ])
        df_listings.to_csv(LISTINGS_CSV, index=False)
    if not os.path.exists(USERS_CSV):
        df_users = pd.DataFrame(columns=["email", "password", "full_name"])
        df_users.to_csv(USERS_CSV, index=False)

def load_listings():
    """Load the listings DataFrame."""
    return pd.read_csv(LISTINGS_CSV)

def load_users():
    """Load the users DataFrame."""
    return pd.read_csv(USERS_CSV)

def save_listings(df):
    """Persist the listings DataFrame."""
    df.to_csv(LISTINGS_CSV, index=False)

def save_users(df):
    """Persist the users DataFrame."""
    df.to_csv(USERS_CSV, index=False)

init_data_files()


# --------------------------------------------------------------------------------
# [2] APP STATE & AUTHENTICATION (SIMPLE DEMO)
# --------------------------------------------------------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "user_email" not in st.session_state:
    st.session_state.user_email = None

def login_user(email, password):
    """Simple function to 'log in' a user (no hashing, not secure)."""
    df_users = load_users()
    user = df_users[(df_users['email'] == email) & (df_users['password'] == password)]
    if len(user) == 1:
        st.session_state.logged_in = True
        st.session_state.user_email = email
        return True
    return False

def logout_user():
    st.session_state.logged_in = False
    st.session_state.user_email = None

def register_user(email, password, full_name):
    """Register a new user (no email validation or security)."""
    df_users = load_users()
    if email in df_users['email'].values:
        st.warning("Email already registered.")
        return
    new_user = pd.DataFrame([{
        "email": email,
        "password": password,
        "full_name": full_name
    }])
    df_users = pd.concat([df_users, new_user], ignore_index=True)
    save_users(df_users)
    st.success("Registration successful! Please log in.")


# --------------------------------------------------------------------------------
# [3] STREAMLIT LAYOUT: SIDEBAR FOR AUTH & NAVIGATION
# --------------------------------------------------------------------------------

st.set_page_config(page_title="Irish Flat Fee Real Estate", layout="wide")

st.sidebar.title("Navigation")

if st.session_state.logged_in:
    st.sidebar.write(f"Logged in as: {st.session_state.user_email}")
    if st.sidebar.button("Log out"):
        logout_user()
        st.experimental_rerun()
else:
    st.sidebar.subheader("Log In")
    email_input = st.sidebar.text_input("Email", value="", key="login_email")
    password_input = st.sidebar.text_input("Password", value="", type="password", key="login_password")
    if st.sidebar.button("Log In"):
        if login_user(email_input, password_input):
            st.sidebar.success("Logged in successfully!")
            st.experimental_rerun()
        else:
            st.sidebar.error("Invalid credentials")

    st.sidebar.subheader("Register")
    reg_email = st.sidebar.text_input("Email", value="", key="reg_email")
    reg_password = st.sidebar.text_input("Password", value="", type="password", key="reg_password")
    reg_full_name = st.sidebar.text_input("Full Name", value="", key="reg_name")
    if st.sidebar.button("Register"):
        register_user(reg_email, reg_password, reg_full_name)

page = st.sidebar.selectbox(
    "Go to",
    ["Home", "List a Property", "My Listings", "Partner Law Firm", "About"]
)


# --------------------------------------------------------------------------------
# [4] PAGE: HOME (LIST OF ALL PROPERTIES)
# --------------------------------------------------------------------------------

def home_page():
    st.title("Irish Real Estate Marketplace (Flat Fee)")
    st.markdown("""
    **Welcome** to our real estate platform designed specifically for the **Irish market**. 
    Sell your home **without** real estate agents for a flat fee:
    - **€250** to list
    - **€250** more if/when your property sells
    """)

    df = load_listings()

    # Show only active (not sold) listings in the public Home page
    df_active = df[df["sold"] == False]

    st.subheader(f"Active Listings ({len(df_active)})")
    for idx, row in df_active.iterrows():
        st.markdown(f"### {row['title']}")
        st.write(f"**Address:** {row['address']}")
        st.write(f"**Price:** €{row['price']}")
        st.write(f"**Description:** {row['description']}")
        st.write(f"Listed on: {row['listed_date']}")
        st.markdown("---")


# --------------------------------------------------------------------------------
# [5] PAGE: LIST A PROPERTY
# --------------------------------------------------------------------------------

def list_property_page():
    if not st.session_state.logged_in:
        st.warning("You must be logged in to list a property.")
        return

    st.title("List Your Property")
    st.write("Fill out the details below to post your property for a flat fee of €250.")

    # Form to gather property details
    with st.form("list_property_form"):
        title = st.text_input("Property Title (e.g. '3-Bed Family Home')")
        address = st.text_input("Property Address")
        description = st.text_area("Description")
        price = st.number_input("Asking Price (€)", min_value=0, step=1000)
        
        submitted = st.form_submit_button("Submit Property")

    if submitted:
        if title and address and description and price > 0:
            # In a real app, you'd redirect to a payment gateway here.
            # For this demo, we simulate a payment confirmation step.
            st.info("Please confirm your €250 listing fee payment to proceed.")
            if st.button("Confirm Payment"):
                df = load_listings()
                new_id = len(df) + 1
                new_listing = pd.DataFrame([{
                    "listing_id": new_id,
                    "owner_email": st.session_state.user_email,
                    "title": title,
                    "address": address,
                    "description": description,
                    "price": price,
                    "listed_date": str(date.today()),
                    "paid_listing_fee": True,
                    "sold": False,
                    "paid_selling_fee": False
                }])
                df = pd.concat([df, new_listing], ignore_index=True)
                save_listings(df)
                st.success(f"Your property '{title}' has been listed successfully!")
        else:
            st.error("Please fill all fields correctly.")


# --------------------------------------------------------------------------------
# [6] PAGE: MY LISTINGS (FOR LOGGED-IN USERS)
# --------------------------------------------------------------------------------

def my_listings_page():
    if not st.session_state.logged_in:
        st.warning("You must be logged in to view your listings.")
        return

    st.title("My Listings")
    df = load_listings()
    user_listings = df[df["owner_email"] == st.session_state.user_email]

    if user_listings.empty:
        st.info("You have no listings yet.")
        return

    for idx, row in user_listings.iterrows():
        st.markdown(f"### {row['title']}")
        st.write(f"**Address:** {row['address']}")
        st.write(f"**Price:** €{row['price']}")
        st.write(f"**Description:** {row['description']}")
        st.write(f"**Listing Fee Paid:** {row['paid_listing_fee']}")
        st.write(f"**Sold?:** {row['sold']}")
        st.write(f"**Selling Fee Paid?:** {row['paid_selling_fee']}")
        st.write(f"Listed on {row['listed_date']}")

        # If not sold, user can mark it as sold
        if not row["sold"]:
            if st.button(f"Mark as Sold (ID: {row['listing_id']})", key=f"sell_{row['listing_id']}"):
                # In real app, confirm second €250 payment
                st.info("Please confirm your €250 selling fee payment to finalize.")
                if st.button(f"Confirm Payment (ID: {row['listing_id']})", key=f"confirm_sell_{row['listing_id']}"):
                    df.loc[idx, "sold"] = True
                    df.loc[idx, "paid_selling_fee"] = True
                    save_listings(df)
                    st.success(f"Property '{row['title']}' marked as sold. Congratulations!")
                    st.experimental_rerun()

        st.markdown("---")


# --------------------------------------------------------------------------------
# [7] PAGE: PARTNER LAW FIRM
# --------------------------------------------------------------------------------

def partner_law_firm_page():
    st.title("Partner Law Firm")
    st.markdown("""
    We have partnered with **MyIrishLawPartner LLP**, who provide:
    - **Conveyancing** for residential properties
    - **Title checks** and legal documentation
    - **Professional advice** on Irish property law

    **Contact them** for details on how to finalize the legal process of selling your home.
    """)


# --------------------------------------------------------------------------------
# [8] PAGE: ABOUT
# --------------------------------------------------------------------------------

def about_page():
    st.title("About This Platform")
    st.markdown("""
    This platform is designed to help Irish homeowners sell their properties **without** 
    traditional real estate agents. The **flat fee** structure ensures transparency and 
    affordability for sellers.
    
    **Disclaimer:** This is a prototype demonstrating how you can build a real estate listing 
    platform using Python and Streamlit. For a production-level application, integrate:
    - A secure payment gateway (Stripe, PayPal, etc.)
    - Proper user authentication & data encryption
    - Robust database (PostgreSQL, MySQL, etc.)
    - Additional legal compliance and disclaimers
    """)


# --------------------------------------------------------------------------------
# [9] PAGE ROUTING
# --------------------------------------------------------------------------------

if page == "Home":
    home_page()
elif page == "List a Property":
    list_property_page()
elif page == "My Listings":
    my_listings_page()
elif page == "Partner Law Firm":
    partner_law_firm_page()
elif page == "About":
    about_page()
