import streamlit as st
import pandas as pd

# 1. Give the app a title
st.title("📱 iPhone Price Tracker")
st.write("Monitoring daily price fluctuations for iPhone 15 models.")

# 2. Load the data (The CSV we just made)
# We use Pandas (pd) to read the excel-like file
try:
    df = pd.read_csv("iphone_prices.csv")
    
    # 3. Create a filter sidebar
    # Get unique models from the data
    model_list = df['Model'].unique().tolist()
    # Add an "All" option
    selected_models = st.sidebar.multiselect(
        "Select Models to View",
        options=model_list,
        default=model_list
    )

    # 4. Filter the data based on selection
    if selected_models:
        filtered_df = df[df['Model'].isin(selected_models)]
        
        # 5. Show the Data Table
        st.subheader("Price Data")
        st.dataframe(filtered_df)

        # 6. Show a simple Chart
        st.subheader("Price Trends")
        # A simple bar chart showing Price by Model
        st.bar_chart(filtered_df, x="Model", y="Price")
        
    else:
        st.warning("Please select at least one model from the sidebar.")

except FileNotFoundError:
    st.error("❌ Could not find 'iphone_prices.csv'. Run 'data_generator.py' first!")