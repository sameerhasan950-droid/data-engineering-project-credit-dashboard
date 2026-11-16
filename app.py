import streamlit as st
import pandas as pd


st.set_page_config(page_title="Home Credit Risk Analytics", layout="wide")

st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
""", unsafe_allow_html=True)


st.sidebar.markdown("### 🏦 Home Credit Analytics")
st.sidebar.markdown("---")
page = st.sidebar.radio(
    "Navigation Menu", 
    [
        "Executive Overview", 
        "Bureau Analysis", 
        "Installments & Repayments", 
        "Previous Applications", 
        "Credit Card Balance"
    ]
)
st.sidebar.markdown("---")
st.sidebar.info("Dashboard Status: Live & Optimized")


if page == "Executive Overview":
    st.title("🚀 Home Credit Risk Dashboard")
    st.markdown("### Executive Overview & Portfolio Risk Summary")
    
    col1, col2, col3, col4 = st.columns(4)
    col1.metric(label="Total Core Tables", value="7 Files")
    col2.metric(label="Exploratory Threshold", value="0.50")
    col3.metric(label="Pipeline Tier", value="Silver + Gold")
    col4.metric(label="System Status", value="Healthy")
    
    st.markdown("---")
    st.subheader("📊 Portfolio Dataset Distribution Overview")
    
    
    overview_data = pd.DataFrame({
        'Category': ['Bureau Records', 'Installment History', 'Previous Apps', 'Credit Balances'],
        'Records Count': [1716428, 13605401, 1670214, 3840312]
    })
    st.bar_chart(overview_data.set_index('Category'))

# PAGE : BUREAU ANALYSIS
elif page == "Bureau Analysis":
    st.title("📊 Credit Bureau Analysis")
    st.markdown("Insights into clients' previous credit history from other financial institutions.")
    try:
        df = pd.read_csv('bureau.csv')
        
        col1, col2 = st.columns(2)
        col1.metric("Total Bureau Rows", f"{df.shape[0]:,}")
        col2.metric("Total Features (Columns)", df.shape[1])
        
        st.markdown("---")
        if 'CREDIT_ACTIVE' in df.columns:
            st.subheader("Credit Active Status Distribution")
            active_counts = df['CREDIT_ACTIVE'].value_counts()
            st.bar_chart(active_counts)
            
        st.subheader("📋 Bureau Data Sample")
        st.dataframe(df.head(10), use_container_width=True)
    except Exception as e:
        st.error(f"Error loading bureau data: {e}")

# --- PAGE 3: INSTALLMENTS & REPAYMENTS ---
elif page == "Installments & Repayments":
    st.title("💳 Repayment & Installments Analysis")
    st.markdown("Tracking historical payment behaviors, delays, and installment trends.")
    try:
        df = pd.read_csv('installments_payments.csv')
        
        col1, col2 = st.columns(2)
        col1.metric("Total Installment Records", f"{df.shape[0]:,}")
        col2.metric("Tracked Attributes", df.shape[1])
        
        st.markdown("---")
        if 'DAYS_INSTALMENT' in df.columns:
            st.subheader("Installment Days Sample Trend")
            st.line_chart(df['DAYS_INSTALMENT'].head(50))
            
        st.subheader("📋 Installments Data Sample")
        st.dataframe(df.head(10), use_container_width=True)
    except Exception as e:
        st.error(f"Error loading installments data: {e}")

# --- PAGE 4: PREVIOUS APPLICATIONS ---
elif page == "Previous Applications":
    st.title("📂 Previous Loan Applications")
    st.markdown("Evaluating past loan application decisions, requested amounts, and contract types.")
    try:
        df = pd.read_csv('previous_application.csv')
        
        col1, col2 = st.columns(2)
        col1.metric("Total Past Applications", f"{df.shape[0]:,}")
        col2.metric("Contract Variables", df.shape[1])
        
        st.markdown("---")
        if 'NAME_CONTRACT_TYPE' in df.columns:
            st.subheader("Contract Type Breakdown")
            contract_counts = df['NAME_CONTRACT_TYPE'].value_counts()
            st.bar_chart(contract_counts)
            
        st.subheader("📋 Previous Applications Sample")
        st.dataframe(df.head(10), use_container_width=True)
    except Exception as e:
        st.error(f"Error loading previous applications: {e}")

# --- PAGE 5: CREDIT CARD BALANCE ---
elif page == "Credit Card Balance":
    st.title("💳 Credit Card Balance Analytics")
    st.markdown("Monthly balance snapshots and credit utilization trends.")
    try:
        df = pd.read_csv('credit_card_balance.csv')
        
        col1, col2 = st.columns(2)
        col1.metric("Total Balance Records", f"{df.shape[0]:,}")
        col2.metric("Recorded Metrics", df.shape[1])
        
        st.markdown("---")
        if 'MONTHS_BALANCE' in df.columns:
            st.subheader("Balance Timeline Sample")
            st.line_chart(df['MONTHS_BALANCE'].head(50))
            
        st.subheader("📋 Credit Card Data Sample")
        st.dataframe(df.head(10), use_container_width=True)
    except Exception as e:
        st.error(f"Error loading credit card balance data: {e}")