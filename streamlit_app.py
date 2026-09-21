import pandas as pd
import plotly.express as px
import streamlit as st

# Configure page layout
st.set_page_config(
    page_title="Advanced Financial Dashboard", page_icon="📊", layout="wide"
)

st.title("📊 Advanced Financial & Expense Analytics Dashboard")
st.markdown(
    "Upload your transaction statements or explore the built-in sample"
    " analytics."
)

# Sidebar File Uploader
st.sidebar.header("📁 Data Source")
uploaded_file = st.sidebar.file_uploader(
    "Upload CSV or Excel Statement", type=["csv", "xlsx"]
)

if uploaded_file is not None:
  # Read uploaded file
  try:
    if uploaded_file.name.endswith(".csv"):
      df = pd.read_csv(uploaded_file)
    else:
      df = pd.read_excel(uploaded_file)
    st.sidebar.success("File successfully loaded!")
  except Exception as e:
    st.sidebar.error(f"Error reading file: {e}")
    # Fallback to sample data if error occurs
    df = None
else:
  # Sample itemized dataset if no file uploaded
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
  st.sidebar.info("Using sample data. Upload your own file above anytime.")

# Create Multi-Tabs for Advanced Views
tab1, tab2, tab3 = st.tabs(
    ["📈 Visual Analytics", "📋 Itemized Ledger", "🔍 Search & Filter"]
)

with tab1:
  st.subheader("Spending Breakdown & Proportions")

  col1, col2 = st.columns(2)

  with col1:
    if "Category" in df.columns and "Amount" in df.columns:
      cat_summary = df.groupby("Category")["Amount"].sum().reset_index()
      fig_donut = px.pie(
          cat_summary,
          names="Category",
          values="Amount",
          hole=0.4,
          title="Outflows by Category Proportion",
      )
      st.plotly_chart(fig_donut, use_container_width=True)
    else:
      st.warning(
          "Dataset requires 'Category' and 'Amount' columns for charts."
      )

  with col2:
    if "Month" in df.columns and "Amount" in df.columns:
      monthly_summary = df.groupby("Month")["Amount"].sum().reset_index()
      fig_bar = px.bar(
          monthly_summary,
          x="Month",
          y="Amount",
          title="Total Outflows by Month",
          text_auto="$",
      )
      st.plotly_chart(fig_bar, use_container_width=True)
    else:
      st.warning("Dataset requires 'Month' and 'Amount' columns for charts.")

with tab2:
  st.subheader("Complete Itemized Transaction Log")
  st.dataframe(df, use_container_width=True)

with tab3:
  st.subheader("Dynamic Search & Filter")
  search_term = st.text_input(
      "Filter by keyword (e.g., 'Loan', 'Insurance', 'Powershop')"
  )

  if search_term:
    # Search across text-based columns safely
    text_cols = df.select_dtypes(include=["object"]).columns
    if len(text_cols) > 0:
      mask = df[text_cols].apply(
          lambda col: col.str.contains(search_term, case=False, na=False)
      ).any(axis=1)
      filtered_results = df[mask]
      st.write(f"Found {len(filtered_results)} matching transactions:")
      st.dataframe(filtered_results, use_container_width=True)
    else:
      st.info("No text columns available to search.")
  else:
    st.info("Type a keyword above to look up specific transactions.")
