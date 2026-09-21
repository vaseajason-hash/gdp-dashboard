import pandas as pd
import plotly.express as px
import streamlit as st

# Configure page layout
st.set_page_config(
    page_title="BNZ Joint Billing Dashboard (Jan-Sep 2026)",
    page_icon="📊",
    layout="wide",
)

st.title(
    "📊 BNZ Joint Billing Account (02-0316-0685464-000) — Jan to Sep 2026"
)
st.markdown(
    "Comprehensive itemized transaction tracking sourced from your **BNZ Joint"
    " Billing Account**, covering January through September 2026, broken down"
    " by category, sub-category, and payment type."
)

# Sidebar File Uploader & Filters
st.sidebar.header("📁 Data Source & Filters")
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
  # Extended sample dataset covering January to September 2026 for Joint Billing Account
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
      "Account Source": ["BNZ Joint Billing Account"] * 56,
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
          30851.24,
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
  st.sidebar.info(
      "Loaded Joint Billing Account dataset (Jan–Sep 2026 statement records)."
  )

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
df["Month"] = pd.Categorical(
    df["Month"], categories=month_order, ordered=True
)
df = df.sort_values("Month")

# Sidebar Filters
st.sidebar.markdown("---")
selected_month = st.sidebar.selectbox(
    "Select Month:", ["All Months (Overview)"] + month_order
)

# Quick Focus Particulars Dropdown
focus_options = [
    "Show All Transactions",
    "TOWER Insurance 810131660",
    "HCC 1Sandal25174 1Sandal",
    "POWERSHOP Powershop 904059741",
    "Partners Life Limite 1439227",
    "HOUSING LOAN 892391890003",
    "2degrees Broadband",
]
selected_focus = st.sidebar.selectbox(
    "⚡ Quick Focus Particulars:", focus_options
)

# Apply filters
df_filtered = df.copy()

if selected_month != "All Months (Overview)":
  df_filtered = df_filtered[df_filtered["Month"] == selected_month]

if selected_focus != "Show All Transactions":
  df_filtered = df_filtered[
      df_filtered["Particulars"].str.contains(selected_focus, case=False)
  ]

st.subheader(
    f"📅 Viewing: {selected_month} | Focus: {selected_focus}"
    if selected_focus != "Show All Transactions"
    else f"📅 Viewing: {selected_month}"
)

# Separate outflows for expense metrics
df_outflows = df_filtered[df_filtered["Category"] != "Income"]

# Create Multi-Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Visual Analytics",
    "📋 Detailed Ledger",
    "🏷️ Sub-Category & Payment Breakdown",
    "🔍 Search & Filter",
])

with tab1:
  st.subheader("Outflow Proportions & Trends")
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
    if selected_focus == "Show All Transactions":
      if selected_month == "All Months (Overview)":
        monthly_summary = (
            df_outflows.groupby("Month", observed=False)["Amount"]
            .sum()
            .reset_index()
        )
        fig_bar = px.bar(
            monthly_summary,
            x="Month",
            y="Amount",
            title="Total Outflows by Month",
            text_auto="$",
        )
        st.plotly_chart(fig_bar, use_container_width=True)
      else:
        sub_cat_summary = (
            df_outflows.groupby("Sub-Category")["Amount"].sum().reset_index()
        )
        fig_bar = px.bar(
            sub_cat_summary,
            x="Sub-Category",
            y="Amount",
            title=f"Outflows by Sub-Category ({selected_month})",
            text_auto="$",
        )
        st.plotly_chart(fig_bar, use_container_width=True)
    else:
      item_trend = (
          df_outflows.groupby(["Month", "Particulars"])["Amount"]
          .sum()
          .reset_index()
      )
      fig_bar = px.bar(
          item_trend,
          x="Month",
          y="Amount",
          title=f"Trend for '{selected_focus}' (Jan - Sep)",
          text_auto="$",
      )
      st.plotly_chart(fig_bar, use_container_width=True)

with tab2:
  st.subheader("Statement Itemized Log (Joint Billing Account)")
  st.dataframe(df_filtered, use_container_width=True)

with tab3:
  st.subheader("Drill-Down by Sub-Category & Payment Type")
  if not df_outflows.empty:
    sub_summary = (
        df_outflows.groupby(
            ["Month", "Category", "Sub-Category", "Payment Type"]
        )["Amount"]
        .sum()
        .reset_index()
    )
    st.dataframe(sub_summary, use_container_width=True)

    fig_sub = px.bar(
        df_outflows,
        x="Sub-Category",
        y="Amount",
        color="Category",
        title="Expenses Drill-Down",
        text_auto="$",
    )
    st.plotly_chart(fig_sub, use_container_width=True)
  else:
    st.info("No matching outflow data for this selection.")

with tab4:
  st.subheader("Dynamic Search & Filter")
  search_term = st.text_input("Filter by custom keyword")

  if search_term:
    text_cols = df_filtered.select_dtypes(include=["object"]).columns
    mask = df_filtered[text_cols].apply(
        lambda col: col.str.contains(search_term, case=False, na=False)
    ).any(axis=1)
    filtered_results = df_filtered[mask]
    st.write(f"Found {len(filtered_results)} matching transactions:")
    st.dataframe(filtered_results, use_container_width=True)
  else:
    st.info("Type a keyword above to look up specific items.")
