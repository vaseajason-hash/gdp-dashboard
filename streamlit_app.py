import pandas as pd
import streamlit as st

# Configure page
st.set_page_config(
    page_title="Personal Expense Dashboard", page_icon="💰", layout="wide"
)

st.title("📊 Interactive Expense & Budget Dashboard")
st.markdown(
    "Explore your monthly expenses, category breakdowns, and visual data bars."
)

# Sample dataset representing your monthly totals by category
data = {
    "Month": [
        "January",
        "January",
        "January",
        "January",
        "January",
        "February",
        "February",
        "February",
        "February",
        "February",
        "March",
        "March",
        "March",
        "March",
        "March",
        "April",
        "April",
        "April",
        "April",
        "April",
        "May",
        "May",
        "May",
        "May",
        "May",
        "June",
        "June",
        "June",
        "June",
        "June",
        "July",
        "July",
        "July",
        "July",
        "July",
        "August",
        "August",
        "August",
        "August",
        "August",
    ],
    "Category": [
        "Housing Loans & Rates",
        "Insurance",
        "Utilities & Broadband",
        "Subscriptions",
        "General / Food / Fuel",
        "Housing Loans & Rates",
        "Insurance",
        "Utilities & Broadband",
        "Subscriptions",
        "General / Food / Fuel",
        "Housing Loans & Rates",
        "Insurance",
        "Utilities & Broadband",
        "Subscriptions",
        "General / Food / Fuel",
        "Housing Loans & Rates",
        "Insurance",
        "Utilities & Broadband",
        "Subscriptions",
        "General / Food / Fuel",
        "Housing Loans & Rates",
        "Insurance",
        "Utilities & Broadband",
        "Subscriptions",
        "General / Food / Fuel",
        "Housing Loans & Rates",
        "Insurance",
        "Utilities & Broadband",
        "Subscriptions",
        "General / Food / Fuel",
        "Housing Loans & Rates",
        "Insurance",
        "Utilities & Broadband",
        "Subscriptions",
        "General / Food / Fuel",
        "Housing Loans & Rates",
        "Insurance",
        "Utilities & Broadband",
        "Subscriptions",
        "General / Food / Fuel",
    ],
    "Amount": [
        6145.24,
        612.38,
        175.00,
        58.82,
        7492.84,  # Jan
        6145.24,
        612.38,
        175.00,
        34.33,
        6707.92,  # Feb
        6145.24,
        530.43,
        175.00,
        28.75,
        4931.81,  # Mar
        6145.24,
        612.38,
        175.00,
        32.98,
        4886.77,  # Apr
        6145.24,
        612.38,
        175.00,
        32.98,
        5831.27,  # May
        30851.24,
        612.38,
        175.00,
        40.90,
        4309.37,  # Jun (incl. principal)
        6145.24,
        636.38,
        175.00,
        34.94,
        5084.07,  # Jul
        6145.24,
        636.38,
        175.00,
        42.99,
        5246.96,  # Aug
    ],
}

df = pd.DataFrame(data)

# Sidebar Filters
st.sidebar.header("Filter Options")
selected_month = st.sidebar.selectbox(
    "Select Month", ["All"] + list(df["Month"].unique())
)
selected_category = st.sidebar.selectbox(
    "Select Category", ["All"] + list(df["Category"].unique())
)

# Apply Filters
filtered_df = df.copy()
if selected_month != "All":
    filtered_df = filtered_df[filtered_df["Month"] == selected_month]
if selected_category != "All":
    filtered_df = filtered_df[filtered_df["Category"] == selected_category]

# Main Dashboard View
col1, col2 = st.columns(2)
with col1:
    total_spent = filtered_df["Amount"].sum()
    st.metric(
        label="Total Outflows (Filtered)", value=f"${total_spent:,.2f}"
    )

with col2:
    avg_spent = (
        filtered_df["Amount"].mean() if not filtered_df.empty else 0.0
    )
    st.metric(label="Average per Category", value=f"${avg_spent:,.2f}")

st.markdown("---")
st.subheader("Detailed Breakdown & Visual Bars")

if not filtered_df.empty:
    # Display as a native interactive dataframe chart or table
    st.dataframe(filtered_df, use_container_width=True)

    # Optional Bar Chart visualization built right into Streamlit
    chart_data = filtered_df.set_index("Category")["Amount"]
    st.bar_chart(chart_data)
else:
    st.warning("No data matches the selected filters.")
