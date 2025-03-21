{% extends "layout.html" %}

{% block content %}
<section class="hero">
    <div class="container">
        <h1>Buy and Sell Properties Directly</h1>
        <p>Cut out the middleman and save thousands on agent fees. Connect directly with buyers and sellers in your area.</p>
        <form action="{{ url_for('all_listings') }}" method="get" class="search-form">
            <input type="text" name="location" placeholder="Enter location, zip code, or address">
            <select name="property_type">
                <option value="">All Properties</option>
                <option value="house">Houses</option>
                <option value="apartment">Apartments</option>
                <option value="condo">Condos</option>
                <option value="land">Land</option>
            </select>
            <select name="price_range">
                <option value="">Any Price</option>
                <option value="under_100k">Under $100k</option>
                <option value="100k_200k">$100k - $200k</option>
                <option value="200k_300k">$200k - $300k</option>
                <option value="300k_500k">$300k - $500k</option>
                <option value="over_500k">$500k+</option>
            </select>
            <button type="submit">Search</button>
        </form>
    </div>
</section>

<section class="features">
    <div class="container">
        <div class="section-heading">
            <h2>Why Choose HomeDirect?</h2>
            <p>Our platform is designed to simplify the real estate process and save you money.</p>
        </div>
        <div class="feature-grid">
            <div class="feature-card">
                <div class="feature-icon">💰</div>
                <h3>Save on Commissions</h3>
                <p>Avoid agent fees that typically cost 5-6% of your property value. Keep more money in your pocket.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">🤝</div>
                <h3>Direct Communication</h3>
                <p>Connect directly with buyers or sellers without a middleman slowing down the process.</p>
            </div>
            <div class="feature-card">
                <div class="feature-icon">📱</div>
                <h3>Easy-to-Use Platform</h3>
                <p>Our intuitive interface makes listing or finding properties simple and stress-free.</p>
            </div>
        </div>
    </div>
</section>

<section class="listings" id="listings">
    <div class="container">
        <div class="section-heading">
            <h2>Featured Listings</h2>
            <p>Browse our latest properties for sale directly from owners.</p>
        </div>
        <div class="listings-grid">
            {% for listing in listings %}
            <div class="listing-card">
                <div class="listing-image" style="background: url('{{ listing.image }}') center/cover;">
                    <div class="listing-price">${{ "{:,.0f}".format(listing.price) }}</div>
                </div>
                <div class="listing-content">
                    <h3 class="listing-title">{{ listing.title }}</h3>
                    <div class="listing-location">
                        📍 {{ listing.location }}
                    </div>
                    <div class="listing-features">
                        <div class="listing-feature">
                            🛏️ {{ listing.bedrooms }} Bedrooms
                        </div>
                        <div class="listing-feature">
                            🚿 {{ listing.bathrooms }} Bathrooms
                        </div>
                        <div class="listing-feature">
                            📏 {{ "{:,.0f}".format(listing.sqft) }} sq ft
                        </div>
                    </div>
                </div>
            </div>
            {% endfor %}
        </div>
        <div style="text-align: center; margin-top: 2rem;">
            <a href="{{ url_for('all_listings') }}" class="btn">View All Listings</a>
        </div>
    </div>
</section>

<section class="how-it-works" id="how-it-works">
    <div class="container">
        <div class="section-heading">
            <h2>How It Works</h2>
            <p>Selling or buying property has never been easier.</p>
        </div>
        <div class="steps">
            <div class="step">
                <h3>Create Your Account</h3>
                <p>Sign up for free and verify your identity to get started on our secure platform.</p>
            </div>
            <div class="step">
                <h3>List Your Property</h3>
                <p>Upload photos, add detailed descriptions, and set your price - all in just minutes.</p>
            </div>
            <div class="step">
                <h3>Connect With Buyers/Sellers</h3>
                <p>Communicate directly through our messaging system to arrange viewings and negotiations.</p>
            </div>
            <div class="step">
                <h3>Close The Deal</h3>
                <p>Use our resources and optional professional services to complete the transaction safely.</p>
            </div>
        </div>
    </div>
</section>

<section class="testimonials" id="testimonials">
    <div class="container">
        <div class="section-heading">
            <h2>What Our Users Say</h2>
            <p>Hear from people who have successfully bought and sold properties on HomeDirect.</p>
        </div>
        <div class="testimonial-grid">
            <div class="testimonial-card">
                <div class="testimonial-content">
                    "I saved over $15,000 by selling my home on HomeDirect instead of using a traditional agent. The process was surprisingly simple, and I found a buyer within just two weeks!"
                </div>
                <div class="testimonial-author">
                    <div class="testimonial-avatar"></div>
                    <div>
                        <div class="testimonial-name">Sarah Johnson</div>
                        <div class="testimonial-role">Home Seller</div>
                    </div>
                </div>
            </div>
            
            <div class="testimonial-card">
                <div class="testimonial-content">
                    "As a first-time homebuyer, I appreciated being able to communicate directly with the seller. We built a rapport that made the whole transaction smoother, and I felt like I got a fair price."
                </div>
                <div class="testimonial-author">
                    <div class="testimonial-avatar"></div>
                    <div>
                        <div class="testimonial-name">Michael Chen</div>
                        <div class="testimonial-role">Home Buyer</div>
                    </div>
                </div>
            </div>

            <div class="testimonial-card">
                <div class="testimonial-content">
                    "The dashboard makes it easy to manage my listings and communicate with potential buyers. I've now sold two properties through HomeDirect and saved thousands in commission fees!"
                </div>
                <div class="testimonial-author">
                    <div class="testimonial-avatar"></div>
                    <div>
                        <div class="testimonial-name">David Rodriguez</div>
                        <div class="testimonial-role">Home Seller</div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="cta">
    <div class="container">
        <h2>Ready to Get Started?</h2>
        <p>Join thousands of satisfied users who have bought and sold properties without the hefty agent fees.</p>
        <div class="cta-buttons">
            <a href="{{ url_for('signup') }}" class="btn btn-white">Sign Up Now</a>
            <a href="{{ url_for('all_listings') }}" class="btn btn-outline">Browse Listings</a>
        </div>
    </div>
</section>
{% endblock %}
