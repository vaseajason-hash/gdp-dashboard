import pandas as pd
import plotly.express as px
import streamlit as st

# Configure page layout
st.set_page_config(
    page_title="BNZ Joint Billing Dashboard (Jan-Sep 2026)",
    page_icon="📊",
    layout="wide",
)

st.title("📊 BNZ Joint Billing Account - Jan to Sep 2026 Analytics")
st.markdown(
    "Comprehensive itemized transaction tracking covering January through"
    " September 2026, broken down by category, sub-category, and payment type."
)

# Sidebar File Uploader
st.sidebar.header("📁 Data Source")
uploaded_file = st.sidebar.file_uploader(
    "Upload CSV or Excel Statement", type=["csv", "xlsx"]
)

if uploaded_file is not None:
  try:
    if uploaded_file.name.endswith(".csv"):
      df = pd.read_csv(uploaded_file)
    else:
      df = pd.read_excel(uploaded_file)
    st.sidebar.success("File successfully loaded!")
  except Exception as e:
    st.sidebar.error(f"Error reading file: {e}")
    df = None
else:
  # Extended sample dataset covering January to September 2026
  data = {
      "Date": [
          # January 2026
          "2026-01-01",
          "2026-01-01",
          "2026-01-01",
          "2026-01-01",
          "2026-01-05",
          "2026-01-06",
          "2026-01-07",
          "2026-01-08",
          # February 2026
          "2026-02-01",
          "2026-02-01",
          "2026-02-05",
          "2026-02-06",
          "2026-02-07",
          "2026-02-08",
          # March 2026
          "2026-03-01",
          "2026-03-01",
          "2026-03-05",
          "2026-03-06",
          "2026-03-07",
          "2026-03-08",
          # April 2026
          "2026-04-01",
          "2026-04-01",
          "2026-04-05",
          "2026-04-06",
          "2026-04-07",
          "2026-04-08",
          # May 2026
          "2026-05-01",
          "2026-05-01",
          "2026-05-05",
          "2026-05-06",
          "2026-05-07",
          "2026-05-08",
          # June 2026
          "2026-06-01",
          "2026-06-01",
          "2026-06-03",
          "2026-06-05",
          "2026-06-06",
          "2026-06-07",
          "2026-06-08",
          # July 2026
          "2026-07-01",
          "2026-07-01",
          "2026-07-05",
          "2026-07-06",
          "2026-07-07",
          "2026-07-08",
          # August 2026
          "2026-08-01",
          "2026-08-01",
          "2026-08-05",
          "2026-08-06",
          "2026-08-07",
          "2026-08-08",
          # September 2026
          "2026-09-01",
          "2026-09-01",
          "2026-09-05",
          "2026-09-06",
          "2026-09-07",
          "2026-09-08",
      ],
      "Month": [
          "January",
          "January",
          "January",
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
          "February",
          "March",
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
          "April",
          "May",
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
          "June",
          "June",
          "July",
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
          "August",
          "September",
          "September",
          "September",
          "September",
          "September",
          "September",
      ],
      "Category": [
          "Insurance",
          "Housing",
          "General/Food",
          "Utilities",
          "Insurance",
          "Income",
          "Housing",
          "Utilities",
          "Insurance",
          "Housing",
          "Insurance",
          "Income",
          "Housing",
          "Utilities",
          "Insurance",
          "Housing",
          "Insurance",
          "Income",
          "Housing",
          "Utilities",
          "Insurance",
          "Housing",
          "Insurance",
          "Income",
          "Housing",
          "Utilities",
          "Insurance",
          "Housing",
          "Insurance",
          "Income",
          "Housing",
          "Utilities",
          "Insurance",
          "Housing",
          "Housing",
          "Insurance",
          "Income",
          "Housing",
          "Utilities",
          "Insurance",
          "Housing",
          "Insurance",
          "Income",
          "Housing",
          "Utilities",
          "Insurance",
          "Housing",
          "Insurance",
          "Income",
          "Housing",
          "Utilities",
          "Insurance",
          "Housing",
          "Insurance",
          "Income",
          "Housing",
          "Utilities",
      ],
      "Sub-Category": [
          "Asset/Other Insurance",
          "Council / Rates",
          "Groceries & Dining",
          "Power & Energy",
          "Life Insurance",
          "Salary / Wages",
          "Mortgage / Loans",
          "Mobile & Broadband",
          "Asset/Other Insurance",
          "Council / Rates",
          "Life Insurance",
          "Salary / Wages",
          "Mortgage / Loans",
          "Mobile & Broadband",
          "Asset/Other Insurance",
          "Council / Rates",
          "Life Insurance",
          "Salary / Wages",
          "Mortgage / Loans",
          "Mobile & Broadband",
          "Asset/Other Insurance",
          "Council / Rates",
          "Life Insurance",
          "Salary / Wages",
          "Mortgage / Loans",
          "Mobile & Broadband",
          "Asset/Other Insurance",
          "Council / Rates",
          "Life Insurance",
          "Salary / Wages",
          "Mortgage / Loans",
          "Mobile & Broadband",
          "Asset/Other Insurance",
          "Council / Rates",
          "Lump-Sum Principal",
          "Life Insurance",
          "Salary / Wages",
          "Mortgage / Loans",
          "Mobile & Broadband",
          "Asset/Other Insurance",
          "Council / Rates",
          "Life Insurance",
          "Salary / Wages",
          "Mortgage / Loans",
          "Mobile & Broadband",
          "Asset/Other Insurance",
          "Council / Rates",
          "Life Insurance",
          "Salary / Wages",
          "Mortgage / Loans",
          "Mobile & Broadband",
          "Asset/Other Insurance",
          "Council / Rates",
          "Life Insurance",
          "Salary / Wages",
          "Mortgage / Loans",
          "Mobile & Broadband",
      ],
      "Particulars": [
          "TOWER Insurance 810131660",
          "HCC 1Sandal25174 1Sandal",
          "WOOLWORTHS NZ / DINING",
          "POWERSHOP Powershop 904059741",
          "Partners Life Limite 1439227",
          "AFFINITY EMPL GWF PAY",
          "HOUSING LOAN 892391890003",
          "2degrees Broadband",
          "TOWER Insurance 810131660",
          "HCC 1Sandal25174 1Sandal",
          "Partners Life Limite 1439227",
          "AFFINITY EMPL GWF PAY",
          "HOUSING LOAN 892391890003",
          "2degrees Broadband",
          "TOWER Insurance 810131660",
          "HCC 1Sandal25174 1Sandal",
          "Partners Life Limite 1439227",
          "AFFINITY EMPL GWF PAY",
          "HOUSING LOAN 892391890003",
          "2degrees Broadband",
          "TOWER Insurance 810131660",
          "HCC 1Sandal25174 1Sandal",
          "Partners Life Limite 1439227",
          "AFFINITY EMPL GWF PAY",
          "HOUSING LOAN 892391890003",
          "2degrees Broadband",
          "TOWER Insurance 810131660",
          "HCC 1Sandal25174 1Sandal",
          "Partners Life Limite 1439227",
          "AFFINITY EMPL GWF PAY",
          "HOUSING LOAN 892391890003",
          "2degrees Broadband",
          "TOWER Insurance 810131660",
          "HCC 1Sandal25174 1Sandal",
          "Extra Principal Transfer",
          "Partners Life Limite 1439227",
          "AFFINITY EMPL GWF PAY",
          "HOUSING LOAN 892391890003",
          "2degrees Broadband",
          "TOWER Insurance 810131660",
          "HCC 1Sandal25174 1Sandal",
          "Partners Life Limite 1439227",
          "AFFINITY EMPL GWF PAY",
          "HOUSING LOAN 892391890003",
          "2degrees Broadband",
          "TOWER Insurance 810131660",
          "HCC 1Sandal25174 1Sandal",
          "Partners Life Limite 1439227",
          "AFFINITY EMPL GWF PAY",
          "HOUSING LOAN 892391890003",
          "2degrees Broadband",
          "TOWER Insurance 810131660",
          "HCC 1Sandal25174 1Sandal",
          "Partners Life Limite 1439227",
          "AFFINITY EMPL GWF PAY",
          "HOUSING LOAN 892391890003",
          "2degrees Broadband",
      ],
      "Payment Type": [
          "Direct Debit (DD)",
          "Direct Debit (DD)",
          "Point of Sale (PS)",
          "Auto-Payment (AP)",
          "Direct Debit (DD)",
          "Direct Credit (DC)",
          "Loan Repayment (LR)",
          "Auto-Payment (AP)",
          "Direct Debit (DD)",
          "Direct Debit (DD)",
          "Direct Debit (DD)",
          "Direct Credit (DC)",
          "Loan Repayment (LR)",
          "Auto-Payment (AP)",
          "Direct Debit (DD)",
          "Direct Debit (DD)",
          "Direct Debit (DD)",
          "Direct Credit (DC)",
          "Loan Repayment (LR)",
          "Auto-Payment (AP)",
          "Direct Debit (DD)",
          "Direct Debit (DD)",
          "Direct Debit (DD)",
          "Direct Credit (DC)",
          "Loan Repayment (LR)",
          "Auto-Payment (AP)",
          "Direct Debit (DD)",
          "Direct Debit (DD)",
          "Direct Debit (DD)",
          "Direct Credit (DC)",
          "Loan Repayment (LR)",
          "Auto-Payment (AP)",
          "Direct Debit (DD)",
          "Direct Debit (DD)",
          "Bank Transfer",
          "Direct Debit (DD)",
          "Direct Credit (DC)",
          "Loan Repayment (LR)",
          "Auto-Payment (AP)",
          "Direct Debit (DD)",
          "Direct Debit (DD)",
          "Direct Debit (DD)",
          "Direct Credit (DC)",
          "Loan Repayment (LR)",
          "Auto-Payment (AP)",
          "Direct Debit (DD)",
          "Direct Debit (DD)",
          "Direct Debit (DD)",
          "Direct Credit (DC)",
          "Loan Repayment (LR)",
          "Auto-Payment (AP)",
          "Direct Debit (DD)",
          "Direct Debit (DD)",
          "Direct Debit (DD)",
          "Direct Credit (DC)",
          "Loan Repayment (LR)",
          "Auto-Payment (AP)",
      ],
      "Amount": [
          59.75,
          72.25,
          150.00,
          175.00,
          52.09,
          -1116.87,
          6145.24,
          25.00,
          59.75,
          72.25,
          52.09,
          -1116.87,
          6145.24,
          25.00,
          59.75,
          72.25,
          52.09,
          -1116.87,
          6145.24,
          25.00,
          59.75,
          72.25,
          52.09,
          -1116.87,
          6145.24,
          25.00,
          59.75,
          72.25,
          52.09,
          -1116.87,
          6145.24,
          25.00,
          59.75,
          72.25,
          30851.24,  # June lump-sum example spike
          52.09,
          -1116.87,
          6145.24,
          25.00,
          59.75,
          72.25,
          52.09,
          -1116.87,
          6145.24,
          25.00,
          59.75,
          72.25,
          52.09,
          -1116.87,
          6145.24,
          25.00,
          59.75,
          72.25,
          52.09,
          -1116.87,
          6145.24,
          25.00,
      ],
  }
  df = pd.DataFrame(data)
  st.sidebar.info("Loaded January–September 2026 sample statement dataset.")

# Filter out income for outflow summaries
df_outflows = df[df["Category"] != "Income"]

# Sort month order cleanly
month_order = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
]
df_outflows["Month"] = pd.Categorical(
    df_outflows["Month"], categories=month_order, ordered=True
)
df["Month"] = pd.Categorical(
    df["Month"], categories=month_order, ordered=True
)
df_outflows = df_outflows.sort_values("Month")
df = df.sort_values("Month")

# Create Multi-Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Visual Analytics",
    "📋 Detailed Ledger",
    "🏷️ Sub-Category Breakdown",
    "🔍 Search & Filter",
])

with tab1:
  st.subheader("Outflow Proportions & Monthly Trends (Jan - Sep 2026)")
  col1, col2 = st.columns(2)

  with col1:
    cat_summary = df_outflows.groupby("Category")["Amount"].sum().reset_index()
    fig_donut = px.pie(
        cat_summary,
        names="Category",
        values="Amount",
        hole=0.4,
        title="Outflows by Main Category",
    )
    st.plotly_chart(fig_donut, use_container_width=True)

  with col2:
    monthly_summary = (
        df_outflows.groupby("Month", observed=False)["Amount"]
        .sum()
        .reset_index()
    )
    fig_bar = px.bar(
        monthly_summary,
        x="Month",
        y="Amount",
        title="Total Outflows by Month (Jan - Sep)",
        text_auto="$",
    )
    st.plotly_chart(fig_bar, use_container_width=True)

with tab2:
  st.subheader("Complete Statement Itemized Log (Jan - Sep)")
  st.dataframe(df, use_container_width=True)

with tab3:
  st.subheader("Drill-Down by Sub-Category & Payment Type")
  sub_summary = (
      df_outflows.groupby(["Category", "Sub-Category", "Payment Type"])[
          "Amount"
      ]
      .sum()
      .reset_index()
  )
  st.dataframe(sub_summary, use_container_width=True)

  fig_sub = px.bar(
      df_outflows,
      x="Sub-Category",
      y="Amount",
      color="Category",
      title="Expenses by Sub-Category",
      text_auto="$",
  )
  st.plotly_chart(fig_sub, use_container_width=True)

with tab4:
  st.subheader("Dynamic Search & Filter")
  search_term = st.text_input(
      "Filter by keyword (e.g., 'TOWER', 'Loan', 'Direct Debit')"
  )

  if search_term:
    text_cols = df.select_dtypes(include=["object"]).columns
    mask = df[text_cols].apply(
        lambda col: col.str.contains(search_term, case=False, na=False)
    ).any(axis=1)
    filtered_results = df[mask]
    st.write(f"Found {len(filtered_results)} matching transactions:")
    st.dataframe(filtered_results, use_container_width=True)
  else:
    st.info("Type a keyword above to look up specific items across Jan–Sep.")
