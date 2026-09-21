import pandas as pd
import plotly.express as px
import streamlit as st

# Configure page layout
st.set_page_config(
    page_title="BNZ Joint Billing Dashboard (Jan 2026 Complete)",
    page_icon="📊",
    layout="wide",
)

st.title(
    "📊 BNZ Joint Billing Account (02-0316-0685464-000) — January 2026"
)
st.markdown(
    "Complete itemized transaction ledger for **January 2026** sourced directly"
    " from your BNZ Joint Billing statement, broken down by category,"
    " sub-category, and payment type."
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
  # Complete itemized dataset for January 2026 using row records to prevent any length mismatch
  data = [
      {
          "Date": "2026-01-01",
          "Month": "January",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Insurance",
          "Sub-Category": "Asset/Other Insurance",
          "Particulars": "TOWER Insurance 810131660",
          "Payment Type": "Direct Debit (DD)",
          "Amount": 17.67,
      },
      {
          "Date": "2026-01-01",
          "Month": "January",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Insurance",
          "Sub-Category": "Asset/Other Insurance",
          "Particulars": "TOWER Insurance 820056152",
          "Payment Type": "Direct Debit (DD)",
          "Amount": 42.08,
      },
      {
          "Date": "2026-01-01",
          "Month": "January",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Housing",
          "Sub-Category": "Council / Rates",
          "Particulars": "HCC 1Sandal25174 1Sandal",
          "Payment Type": "Direct Debit (DD)",
          "Amount": 72.25,
      },
      {
          "Date": "2026-01-01",
          "Month": "January",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "General/Food",
          "Sub-Category": "Groceries",
          "Particulars": "WOOLWORTHS NZ/47 WHA 6921",
          "Payment Type": "Point of Sale (PS)",
          "Amount": 28.24,
      },
      {
          "Date": "2026-01-01",
          "Month": "January",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "General/Food",
          "Sub-Category": "Dining Out",
          "Particulars": "CAMEL KEBAB NAWTON 6921",
          "Payment Type": "Point of Sale (PS)",
          "Amount": 27.30,
      },
      {
          "Date": "2026-01-01",
          "Month": "January",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "General/Food",
          "Sub-Category": "Dining Out",
          "Particulars": "TANK TE AWA MALL 6921",
          "Payment Type": "Point of Sale (PS)",
          "Amount": 9.50,
      },
      {
          "Date": "2026-01-01",
          "Month": "January",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "General/Food",
          "Sub-Category": "Fuel / Transport",
          "Particulars": "Waitomo App 6921",
          "Payment Type": "Point of Sale (PS)",
          "Amount": 30.00,
      },
      {
          "Date": "2026-01-01",
          "Month": "January",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "General/Food",
          "Sub-Category": "Dining Out",
          "Particulars": "ROBERT HARRIS TE AWA 6921",
          "Payment Type": "Point of Sale (PS)",
          "Amount": 14.50,
      },
      {
          "Date": "2026-01-01",
          "Month": "January",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "General/Food",
          "Sub-Category": "Dining Out",
          "Particulars": "DOMINOS NAWTON 6921",
          "Payment Type": "Point of Sale (PS)",
          "Amount": 11.14,
      },
      {
          "Date": "2026-01-01",
          "Month": "January",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "General/Food",
          "Sub-Category": "Dining Out",
          "Particulars": "SUSHI TIME 6921",
          "Payment Type": "Point of Sale (PS)",
          "Amount": 23.38,
      },
      {
          "Date": "2026-01-01",
          "Month": "January",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "General/Food",
          "Sub-Category": "Dining Out",
          "Particulars": "WHANG THAI 2 6921",
          "Payment Type": "Point of Sale (PS)",
          "Amount": 20.40,
      },
      {
          "Date": "2026-01-01",
          "Month": "January",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Housing",
          "Sub-Category": "Council / Rates",
          "Particulars": "Regional Rate Rates",
          "Payment Type": "Auto-Payment (AP)",
          "Amount": 15.26,
      },
      {
          "Date": "2026-01-01",
          "Month": "January",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Utilities",
          "Sub-Category": "Mobile & Broadband",
          "Particulars": "TWO DEGREES MOBILE AUTO PAYMENT",
          "Payment Type": "Auto-Payment (AP)",
          "Amount": 24.00,
      },
      {
          "Date": "2026-01-01",
          "Month": "January",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Utilities",
          "Sub-Category": "Power & Energy",
          "Particulars": "POWERSHOP Powershop 904059741",
          "Payment Type": "Auto-Payment (AP)",
          "Amount": 50.00,
      },
      {
          "Date": "2026-01-05",
          "Month": "January",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Insurance",
          "Sub-Category": "Life Insurance",
          "Particulars": "Partners Life Limite 1439227 PartnersLife",
          "Payment Type": "Direct Debit (DD)",
          "Amount": 52.09,
      },
      {
          "Date": "2026-01-05",
          "Month": "January",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Housing",
          "Sub-Category": "Mortgage / Loans",
          "Particulars": "HOUSING LOAN 892391890003",
          "Payment Type": "Loan Repayment (LR)",
          "Amount": 361.51,
      },
      {
          "Date": "2026-01-05",
          "Month": "January",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Housing",
          "Sub-Category": "Mortgage / Loans",
          "Particulars": "HOUSING LOAN 892391890005",
          "Payment Type": "Loan Repayment (LR)",
          "Amount": 363.18,
      },
      {
          "Date": "2026-01-06",
          "Month": "January",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Income",
          "Sub-Category": "Salary / Wages",
          "Particulars": "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON",
          "Payment Type": "Direct Credit (DC)",
          "Amount": -1116.87,
      },
      {
          "Date": "2026-01-07",
          "Month": "January",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Housing",
          "Sub-Category": "Mortgage / Loans",
          "Particulars": "HOUSING LOAN 892391890004",
          "Payment Type": "Loan Repayment (LR)",
          "Amount": 13.31,
      },
      {
          "Date": "2026-01-07",
          "Month": "January",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Utilities",
          "Sub-Category": "Mobile & Broadband",
          "Particulars": "2degrees Broadband 2degreesBroa 10695125",
          "Payment Type": "Auto-Payment (AP)",
          "Amount": 25.00,
      },
      {
          "Date": "2026-01-08",
          "Month": "January",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Insurance",
          "Sub-Category": "Life Insurance",
          "Particulars": "Partners Life Limite 1439227 PartnersLife",
          "Payment Type": "Direct Debit (DD)",
          "Amount": 52.09,
      },
      {
          "Date": "2026-01-08",
          "Month": "January",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Insurance",
          "Sub-Category": "Asset/Other Insurance",
          "Particulars": "TOWER Insurance 820056152",
          "Payment Type": "Direct Debit (DD)",
          "Amount": 64.39,
      },
      {
          "Date": "2026-01-08",
          "Month": "January",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Housing",
          "Sub-Category": "Council / Rates",
          "Particulars": "HCC 1Sandal25174 1Sandal",
          "Payment Type": "Direct Debit (DD)",
          "Amount": 72.25,
      },
      {
          "Date": "2026-01-08",
          "Month": "January",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Housing",
          "Sub-Category": "Council / Rates",
          "Particulars": "Regional Rate Rates",
          "Payment Type": "Auto-Payment (AP)",
          "Amount": 15.26,
      },
  ]
  df = pd.DataFrame(data)
  st.sidebar.info("Loaded January 2026 BNZ Joint Billing statement.")

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

# Dynamically populate Quick Focus Particulars with ALL unique particulars from dataset
unique_particulars = sorted(df["Particulars"].dropna().unique().tolist())
focus_options = ["Show All Transactions"] + unique_particulars

selected_focus = st.sidebar.selectbox(
    "⚡ Quick Focus Particulars (All Outgoing):", focus_options
)

# Apply filters
df_filtered = df.copy()

if selected_month != "All Months (Overview)":
  df_filtered = df_filtered[df_filtered["Month"] == selected_month]

if selected_focus != "Show All Transactions":
  df_filtered = df_filtered[df_filtered["Particulars"] == selected_focus]

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
      sub_cat_summary = (
          df_outflows.groupby("Sub-Category")["Amount"].sum().reset_index()
      )
      fig_bar = px.bar(
          sub_cat_summary,
          x="Sub-Category",
          y="Amount",
          title="Outflows by Sub-Category (January)",
          text_auto="$",
      )
      st.plotly_chart(fig_bar, use_container_width=True)
    else:
      item_trend = (
          df_outflows.groupby(["Date", "Particulars"])["Amount"]
          .sum()
          .reset_index()
      )
      fig_bar = px.bar(
          item_trend,
          x="Date",
          y="Amount",
          title=f"Transactions for '{selected_focus}' in January",
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
            ["Date", "Category", "Sub-Category", "Payment Type"]
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
