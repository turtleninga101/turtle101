<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>HomeDirect - Property Marketplace</title>
    <style>
        :root {
            --primary: #2563eb;
            --primary-dark: #1d4ed8;
            --secondary: #f59e0b;
            --light: #f3f4f6;
            --dark: #1f2937;
            --success: #22c55e;
            --danger: #ef4444;
        }
        
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        }
        
        body {
            background-color: #f9fafb;
            color: var(--dark);
            line-height: 1.6;
        }
        
        .container {
            width: 100%;
            max-width: 1200px;
            margin: 0 auto;
            padding: 0 20px;
        }
        
        header {
            background-color: white;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            position: sticky;
            top: 0;
            z-index: 100;
        }
        
        nav {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 1rem 0;
        }
        
        .logo {
            font-size: 1.5rem;
            font-weight: bold;
            color: var(--primary);
        }
        
        .logo span {
            color: var(--secondary);
        }
        
        .nav-links {
            display: flex;
            gap: 1.5rem;
        }
        
        .nav-links a {
            text-decoration: none;
            color: var(--dark);
            font-weight: 500;
            transition: color 0.3s;
        }
        
        .nav-links a:hover {
            color: var(--primary);
        }
        
        .btn {
            display: inline-block;
            padding: 0.5rem 1rem;
            background-color: var(--primary);
            color: white;
            border-radius: 0.25rem;
            text-decoration: none;
            font-weight: 500;
            transition: background-color 0.3s;
            border: none;
            cursor: pointer;
        }
        
        .btn:hover {
            background-color: var(--primary-dark);
        }
        
        .btn-outline {
            background-color: transparent;
            border: 1px solid var(--primary);
            color: var(--primary);
        }
        
        .btn-outline:hover {
            background-color: var(--primary);
            color: white;
        }
        
        .hero {
            background: linear-gradient(rgba(0, 0, 0, 0.5), rgba(0, 0, 0, 0.5)), url('/api/placeholder/1200/600') center/cover;
            color: white;
            padding: 5rem 0;
            text-align: center;
        }
        
        .hero h1 {
            font-size: 3rem;
            margin-bottom: 1rem;
        }
        
        .hero p {
            font-size: 1.2rem;
            margin-bottom: 2rem;
            max-width: 600px;
            margin-left: auto;
            margin-right: auto;
        }
        
        .search-form {
            display: flex;
            background-color: white;
            border-radius: 0.5rem;
            overflow: hidden;
            max-width: 800px;
            margin: 0 auto;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .search-form input {
            flex: 1;
            padding: 1rem;
            border: none;
            outline: none;
            font-size: 1rem;
        }
        
        .search-form select {
            padding: 1rem;
            border: none;
            border-left: 1px solid #e5e7eb;
            outline: none;
            font-size: 1rem;
        }
        
        .search-form button {
            padding: 1rem 1.5rem;
            background-color: var(--primary);
            color: white;
            border: none;
            cursor: pointer;
            font-weight: 500;
        }
        
        .features {
            padding: 5rem 0;
        }
        
        .section-heading {
            text-align: center;
            margin-bottom: 3rem;
        }
        
        .section-heading h2 {
            font-size: 2rem;
            color: var(--dark);
            margin-bottom: 1rem;
        }
        
        .section-heading p {
            color: #6b7280;
            max-width: 600px;
            margin: 0 auto;
        }
        
        .feature-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }
        
        .feature-card {
            background-color: white;
            border-radius: 0.5rem;
            padding: 2rem;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
            text-align: center;
        }
        
        .feature-icon {
            width: 60px;
            height: 60px;
            background-color: var(--light);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            margin: 0 auto 1.5rem;
            color: var(--primary);
            font-size: 1.5rem;
        }
        
        .feature-card h3 {
            margin-bottom: 1rem;
            color: var(--dark);
        }
        
        .feature-card p {
            color: #6b7280;
        }
        
        .listings {
            padding: 5rem 0;
            background-color: var(--light);
        }
        
        .listings-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }
        
        .listing-card {
            background-color: white;
            border-radius: 0.5rem;
            overflow: hidden;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        
        .listing-image {
            height: 200px;
            background-color: #e5e7eb;
            position: relative;
        }
        
        .listing-price {
            position: absolute;
            bottom: 1rem;
            left: 1rem;
            background-color: var(--primary);
            color: white;
            padding: 0.5rem 1rem;
            border-radius: 0.25rem;
            font-weight: 500;
        }
        
        .listing-content {
            padding: 1.5rem;
        }
        
        .listing-title {
            font-size: 1.2rem;
            margin-bottom: 0.5rem;
            color: var(--dark);
        }
        
        .listing-location {
            color: #6b7280;
            margin-bottom: 1rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }
        
        .listing-features {
            display: flex;
            justify-content: space-between;
            border-top: 1px solid #e5e7eb;
            padding-top: 1rem;
        }
        
        .listing-feature {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            color: #6b7280;
            font-size: 0.9rem;
        }
        
        .how-it-works {
            padding: 5rem 0;
        }
        
        .steps {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 2rem;
            counter-reset: step;
        }
        
        .step {
            position: relative;
            padding-left: 4rem;
        }
        
        .step::before {
            counter-increment: step;
            content: counter(step);
            position: absolute;
            left: 0;
            top: 0;
            width: 3rem;
            height: 3rem;
            background-color: var(--primary);
            color: white;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            font-weight: bold;
            font-size: 1.5rem;
        }
        
        .step h3 {
            margin-bottom: 1rem;
            color: var(--dark);
        }
        
        .step p {
            color: #6b7280;
        }
        
        .testimonials {
            padding: 5rem 0;
            background-color: var(--light);
        }
        
        .testimonial-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
            gap: 2rem;
        }
        
        .testimonial-card {
            background-color: white;
            border-radius: 0.5rem;
            padding: 2rem;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        
        .testimonial-content {
            margin-bottom: 1.5rem;
            color: #4b5563;
            font-style: italic;
        }
        
        .testimonial-author {
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        
        .testimonial-avatar {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background-color: #e5e7eb;
        }
        
        .testimonial-name {
            font-weight: 500;
            color: var(--dark);
        }
        
        .testimonial-role {
            color: #6b7280;
            font-size: 0.9rem;
        }
        
        .cta {
            padding: 5rem 0;
            text-align: center;
            background-color: var(--primary);
            color: white;
        }
        
        .cta h2 {
            font-size: 2.5rem;
            margin-bottom: 1.5rem;
        }
        
        .cta p {
            max-width: 600px;
            margin: 0 auto 2rem;
            font-size: 1.2rem;
        }
        
        .cta-buttons {
            display: flex;
            gap: 1rem;
            justify-content: center;
        }
        
        .btn-white {
            background-color: white;
            color: var(--primary);
        }
        
        .btn-white:hover {
            background-color: #f3f4f6;
        }
        
        footer {
            background-color: var(--dark);
            color: white;
            padding: 3rem 0;
        }
        
        .footer-grid {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 2rem;
        }
        
        .footer-col h3 {
            font-size: 1.2rem;
            margin-bottom: 1.5rem;
            color: white;
        }
        
        .footer-links {
            list-style: none;
        }
        
        .footer-links li {
            margin-bottom: 0.5rem;
        }
        
        .footer-links a {
            color: #9ca3af;
            text-decoration: none;
            transition: color 0.3s;
        }
        
        .footer-links a:hover {
            color: white;
        }
        
        .footer-bottom {
            margin-top: 3rem;
            text-align: center;
            color: #9ca3af;
            padding-top: 1.5rem;
            border-top: 1px solid #374151;
        }
        
        @media (max-width: 768px) {
            .hero h1 {
                font-size: 2rem;
            }
            
            .search-form {
                flex-direction: column;
            }
            
            .search-form select,
            .search-form input {
                border-left: none;
                border-top: 1px solid #e5e7eb;
            }
            
            .cta-buttons {
                flex-direction: column;
            }
            
            .nav-links {
                display: none;
            }
        }
        
        /* Modal Styles */
        .modal {
            display: none;
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.5);
            z-index: 1000;
            overflow-y: auto;
        }
        
        .modal-content {
            background-color: white;
            margin: 10% auto;
            padding: 2rem;
            border-radius: 0.5rem;
            max-width: 500px;
            position: relative;
        }
        
        .close-modal {
            position: absolute;
            top: 1rem;
            right: 1rem;
            font-size: 1.5rem;
            cursor: pointer;
        }
        
        .form-group {
            margin-bottom: 1.5rem;
        }
        
        .form-group label {
            display: block;
            margin-bottom: 0.5rem;
            font-weight: 500;
        }
        
        .form-group input,
        .form-group textarea,
        .form-group select {
            width: 100%;
            padding: 0.75rem;
            border: 1px solid #d1d5db;
            border-radius: 0.25rem;
            font-size: 1rem;
        }
        
        .form-group textarea {
            min-height: 100px;
            resize: vertical;
        }
        
        .error-message {
            color: var(--danger);
            font-size: 0.9rem;
            margin-top: 0.25rem;
        }
        
        /* File Upload Styles */
        .file-upload {
            border: 2px dashed #d1d5db;
            border-radius: 0.5rem;
            padding: 2rem;
            text-align: center;
        }
        
        .file-upload p {
            margin-bottom: 1rem;
            color: #6b7280;
        }
        
        .uploaded-files {
            display: flex;
            flex-wrap: wrap;
            gap: 0.5rem;
            margin-top: 1rem;
        }
        
        .uploaded-file {
            position: relative;
            width: 100px;
            height: 100px;
            background-color: #e5e7eb;
            border-radius: 0.25rem;
            overflow: hidden;
        }
        
        .remove-file {
            position: absolute;
            top: 0.25rem;
            right: 0.25rem;
            background-color: white;
            border-radius: 50%;
            width: 1.5rem;
            height: 1.5rem;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        }
        
        /* Dashboard Styles */
        .dashboard-container {
            display: grid;
            grid-template-columns: 250px 1fr;
            min-height: calc(100vh - 64px);
        }
        
        .dashboard-sidebar {
            background-color: white;
            border-right: 1px solid #e5e7eb;
            padding: 2rem 1rem;
        }
        
        .dashboard-menu {
            list-style: none;
        }
        
        .dashboard-menu li {
            margin-bottom: 0.5rem;
        }
        
        .dashboard-menu a {
            display: flex;
            align-items: center;
            gap: 0.75rem;
            padding: 0.75rem 1rem;
            border-radius: 0.25rem;
            text-decoration: none;
            color: var(--dark);
            transition: background-color 0.3s;
        }
        
        .dashboard-menu a:hover,
        .dashboard-menu a.active {
            background-color: var(--light);
            color: var(--primary);
        }
        
        .dashboard-menu a.active {
            font-weight: 500;
        }
        
        .dashboard-content {
            padding: 2rem;
        }
        
        .dashboard-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 2rem;
        }
        
        .property-list {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
            gap: 1.5rem;
        }
        
        /* Property Detail Page */
        .property-detail {
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 2rem;
        }
        
        .property-gallery {
            position: relative;
            overflow: hidden;
            border-radius: 0.5rem;
        }
        
        .property-main-image {
            height: 400px;
            background-color: #e5e7eb;
            margin-bottom: 0.5rem;
            border-radius: 0.5rem;
            overflow: hidden;
        }
        
        .property-thumbnails {
            display: flex;
            gap: 0.5rem;
            overflow-x: auto;
        }
        
        .property-thumbnail {
            width: 80px;
            height: 60px;
            background-color: #e5e7eb;
            border-radius: 0.25rem;
            cursor: pointer;
        }
        
        .property-thumbnail.active {
            border: 2px solid var(--primary);
        }
        
        .property-info {
            background-color: white;
            border-radius: 0.5rem;
            padding: 1.5rem;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        
        .contact-seller {
            margin-top: 2rem;
            background-color: white;
            border-radius: 0.5rem;
            padding: 1.5rem;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        
        .property-description {
            margin-top: 2rem;
            background-color: white;
            border-radius: 0.5rem;
            padding: 1.5rem;
            box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
        }
        
        /* Messages Page */
        .messages-container {
            display: grid;
            grid-template-columns: 300px 1fr;
            height: calc(100vh - 64px);
            overflow: hidden;
        }
        
        .message-contacts {
            border-right: 1px solid #e5e7eb;
            overflow-y: auto;
        }
        
        .message-contact {
            display: flex;
            align-items: center;
            gap: 1rem;
            padding: 1rem;
            border-bottom: 1px solid #e5e7eb;
            cursor: pointer;
        }
        
        .message-contact:hover,
        .message-contact.active {
            background-color: var(--light);
        }
        
        .message-contact-avatar {
            width: 50px;
            height: 50px;
            border-radius: 50%;
            background-color: #e5e7eb;
        }
        
        .message-chat {
            display: flex;
            flex-direction: column;
            height: 100%;
        }
        
        .message-header {
            padding: 1rem;
            border-bottom: 1px solid #e5e7eb;
            display: flex;
            align-items: center;
            gap: 1rem;
        }
        
        .message-body {
            flex: 1;
            overflow-y: auto;
            padding: 1rem;
        }
        
        .message {
            max-width: 70%;
            margin-bottom: 1rem;
            padding: 0.75rem 1rem;
            border-radius: 0.5rem;
        }
        
        .message.received {
            background-color: var(--light);
            align-self: flex-start;
        }
        
        .message.sent {
            background-color: var(--primary);
            color: white;
            align-self: flex-end;
        }
        
        .message-footer {
            padding: 1rem;
            border-top: 1px solid #e5e7eb;
            display: flex;
            gap: 0.5rem;
        }
        
        .message-input {
            flex: 1;
            padding: 0.75rem;
            border: 1px solid #d1d5db;
            border-radius: 0.25rem;
            outline: none;
            resize: none;
        }
    </style>
</head>
<body>
    <header>
        <div class="container">
            <nav>
                <div class="logo">Home<span>Direct</span></div>
                <div class="nav-links">
                    <a href="#how-it-works">How It Works</a>
                    <a href="#listings">Browse Listings</a>
                    <a href="#testimonials">Testimonials</a>
                    <a href="#contact">Contact</a>
                </div>
                <div>
                    <button class="btn btn-outline" onclick="openModal('loginModal')">Login</button>
                    <button class="btn" onclick="openModal('signupModal')">Sign Up</button>
                </div>
            </nav>
        </div>
    </header>

    <section class="hero">
        <div class="container">
            <h1>Buy and Sell Properties Directly</h1>
            <p>Cut out the middleman and save thousands on agent fees. Connect directly with buyers and sellers in your area.</p>
            <div class="search-form">
                <input type="text" placeholder="Enter location, zip code, or address">
                <select>
                    <option>All Properties</option>
                    <option>Houses</option>
                    <option>Apartments</option>
                    <option>Condos</option>
                    <option>Land</option>
                </select>
                <select>
                    <option>Any Price</option>
                    <option>Under $100k</option>
                    <option>$100k - $200k</option>
                    <option>$200k - $300k</option>
                    <option>$300k - $500k</option>
                    <option>$500k+</option>
                </select>
                <button>Search</button>
            </div>
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
                <div class="listing-card">
                    <div class="listing-image" style="background: url('/api/placeholder/400/300') center/cover;">
                        <div class="listing-price">$349,000</div>
                    </div>
                    <div class="listing-content">
                        <h3 class="listing-title">Modern Suburban Home</h3>
                        <div class="listing-location">
                            📍 123 Main St, Anytown, USA
                        </div>
                        <div class="listing-features">
                            <div class="listing-feature">
                                🛏️ 3 Bedrooms
                            </div>
                            <div class="listing-feature">
                                🚿 2 Bathrooms
                            </div>
                            <div class="listing-feature">
                                📏 1,850 sq ft
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="listing-card">
                    <div class="listing-image" style="background: url('/api/placeholder/400/300') center/cover;">
                        <div class="listing-price">$275,000</div>
                    </div>
                    <div class="listing-content">
                        <h3 class="listing-title">Cozy Downtown Condo</h3>
                        <div class="listing-location">
                            📍 456 Park Ave, Anytown, USA
                        </div>
                        <div class="listing-features">
                            <div class="listing-feature">
                                🛏️ 2 Bedrooms
                            </div>
                            <div class="listing-feature">
                                🚿 2 Bathrooms
                            </div>
                            <div class="listing-feature">
                                📏 1,200 sq ft
                            </div>
                        </div>
                    </div>
                </div>
                
                <div class="listing-card">
                    <div class="listing-image" style="background: url('/api/placeholder/400/300') center/cover;">
                        <div class="listing-price">$425,000</div>
                    </div>
                    <div class="listing-content">
                        <h3 class="listing-title">Country Farmhouse</h3>
                        <div class="listing-location">
                            📍 789 Rural Route, Countyville, USA
                        </div>
                        <div class="listing-features">
                            <div class="listing-feature">
                                🛏️ 4 Bedrooms
                            </div>
                            <div class="listing-feature">
                                🚿 2.5 Bathrooms
                            </div>
                            <div class="listing-feature">
                                📏 2,400 sq ft
                            </div>
                        </div>
                    </div>
                </div>
            </div>
            <div style="text-align: center; margin-top: 2rem;">
                <a href="#" class="btn">View All Listings</a>
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
