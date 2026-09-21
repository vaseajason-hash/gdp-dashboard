import pandas as pd
import plotly.express as px
import streamlit as st

# Configure page layout
st.set_page_config(
    page_title="Advanced Financial Dashboard", page_icon="📊", layout="wide"
)

st.title("📊 Advanced Financial & Expense Analytics Dashboard")
st.markdown(
    "Explore itemized transactions, multi-tab analytics, and interactive"
    " visualizations."
)

# Itemized transaction dataset
data = {
    "Date": [
        "2026-01-05",
        "2026-01-07",
        "2026-01-10",
        "2026-01-15",
        "2026-02-04",
        "2026-02-08",
        "2026-02-12",
        "2026-03-03",
        "2026-03-09",
        "2026-04-02",
        "2026-05-04",
        "2026-06-03",
        "2026-07-06",
        "2026-08-04",
    ],
    "Month": [
        "January",
        "January",
        "January",
        "January",
        "February",
        "February",
        "February",
        "March",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
    ],
    "Category": [
        "Housing Loans",
        "Insurance",
        "Utilities",
        "General / Food",
        "Housing Loans",
        "Insurance",
        "General / Food",
        "Housing Loans",
        "Utilities",
        "Housing Loans",
        "Housing Loans",
        "Housing Loans (Extra)",
        "Housing Loans",
        "Housing Loans",
    ],
    "Particulars": [
        "Loan Account 0003",
        "Partners Life",
        "Powershop NZ",
        "Whang Thai 2",
        "Loan Account 0003",
        "Tower Insurance",
        "Grocery Store",
        "Loan Account 0003",
        "Powershop NZ",
        "Loan Account 0003",
        "Loan Account 0003",
        "Lump-Sum Principal",
        "Loan Account 0003",
        "Loan Account 0003",
    ],
    "Amount": [
        6145.24,
        612.38,
        175.00,
        7492.84,
        6145.24,
        612.38,
        6707.92,
        6145.24,
        175.00,
        6145.24,
        6145.24,
        30851.24,
        6145.24,
        6145.24,
    ],
}

df = pd.DataFrame(data)

# Create Multi-Tabs for Advanced Views
tab1, tab2, tab3 = st.tabs(
    ["📈 Visual Analytics", "📋 Itemized Ledger", "🔍 Search & Filter"]
)

with tab1:
    st.subheader("Spending Breakdown & Proportions")

    col1, col2 = st.columns(2)

    with col1:
        # Category Summary for Donut Chart
        cat_summary = df.groupby("Category")["Amount"].sum().reset_index()
        fig_donut = px.pie(
            cat_summary,
            names="Category",
            values="Amount",
            hole=0.4,
            title="Outflows by Category Proportion",
        )
        st.plotly_chart(fig_donut, use_container_width=True)

    with col2:
        # Monthly Bar Chart using Plotly
        monthly_summary = df.groupby("Month")["Amount"].sum().reset_index()
        fig_bar = px.bar(
            monthly_summary,
            x="Month",
            y="Amount",
            title="Total Outflows by Month",
            text_auto="$",
        )
        st.plotly_chart(fig_bar, use_container_width=True)

with tab2:
    st.subheader("Complete Itemized Transaction Log")
    st.dataframe(df, use_container_width=True)

with tab3:
    st.subheader("Dynamic Search & Filter")
    search_term = st.text_input(
        "Filter by keyword (e.g., 'Loan', 'Insurance', 'Powershop')"
    )

    if search_term:
        filtered_results = df[
            df["Particulars"].str.contains(search_term, case=False, na=False)
            | df["Category"].str.contains(search_term, case=False, na=False)
        ]
        st.write(f"Found {len(filtered_results)} matching transactions:")
        st.dataframe(filtered_results, use_container_width=True)
    else:
        st.info("Type a keyword above to look up specific transactions.")
