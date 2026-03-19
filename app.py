import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle
import os

# Set page config
st.set_page_config(
    page_title="Ad Revenue Predictor",
    page_icon="📊",
    layout="centered"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
    }
    .stApp {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
    }
    </style>
    """, unsafe_allow_html=True)

# Train and save model if it doesn't exist
if not os.path.exists('model.pkl'):
    # Simple Data - Website Visitors vs Ad Revenue (in ₹)
    data = {'visitors': [1000, 2500, 5000, 7500, 10000], 
            'revenue': [500, 1250, 2500, 3750, 5000]}
    df = pd.DataFrame(data)
    
    model = LinearRegression().fit(df[['visitors']], df['revenue'])
    
    # Save model
    with open('model.pkl', 'wb') as f:
        pickle.dump(model, f)

# Load the model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# App Header
st.title("📊 Advertisement Revenue Predictor")
st.markdown("### Predict your daily ad revenue based on website traffic")
st.markdown("---")

# Create two columns for better layout
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("#### Enter Website Details")
    
    # Input field
    visitors = st.number_input(
        "Daily Website Visitors",
        min_value=0,
        max_value=100000,
        value=5000,
        step=100,
        help="Enter the number of daily visitors to your website"
    )
    
    # Predict button
    if st.button("Calculate Revenue", type="primary", use_container_width=True):
        # Make prediction
        prediction = model.predict([[visitors]])[0]
        
        # Display result
        st.markdown("---")
        st.success(f"### 💰 Predicted Daily Revenue: ₹{prediction:,.2f}")
        
        # Additional insights
        monthly_revenue = prediction * 30
        yearly_revenue = prediction * 365
        
        st.info(f"""
        **Revenue Projections:**
        - Monthly: ₹{monthly_revenue:,.2f}
        - Yearly: ₹{yearly_revenue:,.2f}
        """)

with col2:
    st.markdown("#### Example")
    st.info("""
    **Sample Data:**
    
    5,000 visitors  
    = ₹2,500/day
    
    10,000 visitors  
    = ₹5,000/day
    """)

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: white;'>
        <p>Built with Streamlit | ML Capstone Project</p>
    </div>
    """, unsafe_allow_html=True)

# Sidebar with info
with st.sidebar:
    st.header("About")
    st.write("""
    This app uses **Linear Regression** to predict advertisement revenue based on website traffic.
    
    **How it works:**
    - More visitors → More ad impressions
    - More impressions → More clicks
    - More clicks → Higher revenue
    
    **Model Details:**
    - Algorithm: Linear Regression
    - Relationship: Revenue = 0.5 × Visitors
    """)
    
    st.header("Model Training Data")
    training_data = pd.DataFrame({
        'Visitors': [1000, 2500, 5000, 7500, 10000],
        'Revenue (₹)': [500, 1250, 2500, 3750, 5000]
    })
    st.dataframe(training_data, use_container_width=True)
