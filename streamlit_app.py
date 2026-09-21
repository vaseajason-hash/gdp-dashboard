import pandas as pd
import streamlit as st

# Configure page layout
st.set_page_config(
    page_title="Detailed Expense Dashboard", page_icon="📊", layout="wide"
)

st.title("📊 Detailed Financial & Expense Tracking Dashboard")
st.markdown(
    "Explore itemized transactions, filter by specific particulars, and"
    " analyze spending patterns."
)

# Expanded itemized dataset (sample structure for individual transactions)
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

# Create Multi-Tabs
tab1, tab2, tab3 = st.tabs(
    ["📋 Itemized Transactions", "📈 Category Breakdown", "🔍 Search & Filter"]
)

with tab1:
    st.subheader("Complete Itemized Log")
    st.dataframe(df, use_container_width=True)

with tab2:
    st.subheader("Spending by Category")
    category_summary = df.groupby("Category")["Amount"].sum().reset_index()
    st.dataframe(category_summary, use_container_width=True)
    st.bar_chart(category_summary.set_index("Category")["Amount"])

with tab3:
    st.subheader("Advanced Search")
    search_term = st.text_input(
        "Search particulars or categories (e.g., 'Loan', 'Insurance', 'Powershop')"
    )

    if search_term:
        filtered_results = df[
            df["Particulars"].str.contains(search_term, case=False, na=False)
            | df["Category"].str.contains(search_term, case=False, na=False)
        ]
        st.write(f"Found {len(filtered_results)} matching transactions:")
        st.dataframe(filtered_results, use_container_width=True)
    else:
        st.info("Type a keyword above to filter transactions.")
