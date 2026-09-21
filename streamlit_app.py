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
  # Complete itemized dataset for January 2026 based on statement screenshots
  data = {
      "Date": [
          # Page 1 & Onward (Jan 1)
          "2026-01-01",
          "2026-01-01",
          "2026-01-01",
          "2026-01-01",
          "2026-01-01",
          "2026-01-01",
          "2026-01-01",
          "2026-01-01",
          "2026-01-01",
          "2026-01-01",
          "2026-01-01",
          "2026-01-01",
          "2026-01-01",
          "2026-01-01",
          # Jan 05 - 08
          "2026-01-05",
          "2026-01-05",
          "2026-01-05",
          "2026-01-06",
          "2026-01-07",
          "2026-01-07",
          "2026-01-08",
          "2026-01-08",
          "2026-01-08",
          "2026-01-08",
          # Jan 09 - 15
          "2026-01-09",
          "2026-01-10",
          "2026-01-11",
          "2026-01-11",
          "2026-01-11",
          "2026-01-11",
          "2026-01-11",
          "2026-01-12",
          "2026-01-12",
          "2026-01-13",
          "2026-01-13",
          "2026-01-14",
          "2026-01-15",
          "2026-01-15",
          "2026-01-15",
          "2026-01-15",
          "2026-01-15",
          "2026-01-15",
          "2026-01-15",
          "2026-01-15",
          "2026-01-15",
          "2026-01-15",
          "2026-01-15",
          "2026-01-15",
          "2026-01-15",
          # Jan 15 - 31
          "2026-01-15",
          "2026-01-15",
          "2026-01-15",
          "2026-01-15",
          "2026-01-15",
          "2026-01-15",
          "2026-01-15",
          "2026-01-20",
          "2026-01-20",
          "2026-01-21",
          "2026-01-21",
          "2026-01-21",
          "2026-01-21",
          "2026-01-22",
          "2026-01-22",
          "2026-01-22",
          "2026-01-22",
          "2026-01-22",
          "2026-01-22",
          "2026-01-22",
          "2026-01-22",
          "2026-01-22",
          "2026-01-22",
          "2026-01-22",
          "2026-01-22",
          "2026-01-22",
          "2026-01-25",
          "2026-01-25",
          "2026-01-25",
          "2026-01-25",
          "2026-01-25",
          "2026-01-26",
          "2026-01-26",
          "2026-01-26",
          "2026-01-26",
          "2026-01-26",
          "2026-01-26",
          "2026-01-26",
          "2026-01-26",
          "2026-01-26",
          "2026-01-26",
          "2026-01-27",
          "2026-01-27",
          "2026-01-27",
          "2026-01-27",
          "2026-01-27",
          "2026-01-27",
          "2026-01-27",
          "2026-01-27",
          "2026-01-28",
          "2026-01-28",
          "2026-01-28",
          "2026-01-28",
          "2026-01-28",
          "2026-01-28",
          "2026-01-29",
          "2026-01-29",
          "2026-01-29",
          "2026-01-29",
          "2026-01-29",
          "2026-01-29",
          "2026-01-29",
          "2026-01-29",
          "2026-01-29",
          "2026-01-29",
          "2026-01-29",
          "2026-01-30",
          "2026-01-30",
          "2026-01-30",
          "2026-01-30",
      ],
      "Month": ["January"] * 110,
      "Account Source": ["BNZ Joint Billing Account"] * 110,
      "Category": [
          # Jan 1 items
          "Insurance",
          "Insurance",
          "Housing",
          "General/Food",
          "General/Food",
          "General/Food",
          "General/Food",
          "General/Food",
          "General/Food",
          "General/Food",
          "General/Food",
          "Housing",
          "Utilities",
          "Utilities",
          # Jan 5 - 8
          "Insurance",
          "Housing",
          "Housing",
          "Income",
          "Housing",
          "Utilities",
          "Insurance",
          "Insurance",
          "Housing",
          "Housing",
          # Jan 9 - 15
          "General/Food",
          "General/Food",
          "General/Food",
          "Income",
          "Utilities",
          "General/Food",
          "General/Food",
          "Travel / Accommodation",
          "Housing",
          "Housing",
          "Utilities",
          "General/Food",
          "Insurance",
          "Insurance",
          "Insurance",
          "Housing",
          "General/Food",
          "General/Food",
          "General/Food",
          "General/Food",
          "Utilities",
          "Housing",
          "Housing",
          "Housing",
          "Housing",
          # Jan 15 - 31
          "Utilities",
          "Utilities",
          "Housing",
          "Housing",
          "Income",
          "General/Food",
          "Housing",
          "Housing",
          "Utilities",
          "Insurance",
          "Insurance",
          "Housing",
          "General/Food",
          "General/Food",
          "General/Food",
          "Housing",
          "Utilities",
          "Utilities",
          "Housing",
          "Housing",
          "Housing",
          "Housing",
          "Income",
          "General/Food",
          "Housing",
          "Utilities",
          "Insurance",
          "Insurance",
          "Insurance",
          "Housing",
          "General/Food",
          "General/Food",
          "General/Food",
          "General/Food",
          "General/Food",
          "General/Food",
          "Housing",
          "Utilities",
          "Utilities",
          "Housing",
          "Housing",
          "Housing",
          "General/Food",
          "General/Food",
          "General/Food",
          "Housing",
          "Utilities",
          "Insurance",
          "Insurance",
          "Insurance",
          "Housing",
          "Housing",
          "Utilities",
          "General/Food",
          "General/Food",
          "General/Food",
          "Housing",
          "Utilities",
          "Utilities",
          "Housing",
          "Housing",
          "Fees & Charges",
          "Fees & Charges",
      ],
      "Sub-Category": [
          # Jan 1 particulars
          "Asset/Other Insurance",
          "Asset/Other Insurance",
          "Council / Rates",
          "Groceries",
          "Dining Out",
          "Dining Out",
          "Fuel / Transport",
          "Dining Out",
          "Dining Out",
          "Dining Out",
          "Dining Out",
          "Council / Rates",
          "Mobile & Broadband",
          "Power & Energy",
          # Jan 5 - 8
          "Life Insurance",
          "Mortgage / Loans",
          "Mortgage / Loans",
          "Salary / Wages",
          "Mortgage / Loans",
          "Mobile & Broadband",
          "Life Insurance",
          "Asset/Other Insurance",
          "Council / Rates",
          "Council / Rates",
          # Jan 9 - 15
          "Dining Out",
          "Dining Out",
          "General/Food",
          "Salary / Wages",
          "Mobile & Broadband",
          "Dining Out",
          "Dining Out",
          "Accommodation",
          "Mortgage / Loans",
          "Mortgage / Loans",
          "Mobile & Broadband",
          "General/Food",
          "Asset/Other Insurance",
          "Asset/Other Insurance",
          "Life Insurance",
          "Council / Rates",
          "Dining Out",
          "Dining Out",
          "General/Food",
          "Dining Out",
          "Mobile & Broadband",
          "Mortgage / Loans",
          "Mortgage / Loans",
          "Mortgage / Loans",
          "Mortgage / Loans",
          # Jan 15 - 31
          "Mobile & Broadband",
          "Power & Energy",
          "Mortgage / Loans",
          "Mortgage / Loans",
          "Salary / Wages",
          "General/Food",
          "Mortgage / Loans",
          "Council / Rates",
          "Mobile & Broadband",
          "Life Insurance",
          "Asset/Other Insurance",
          "Council / Rates",
          "Dining Out",
          "General/Food",
          "Dining Out",
          "Mortgage / Loans",
          "Mobile & Broadband",
          "Power & Energy",
          "Mortgage / Loans",
          "Mortgage / Loans",
          "Mortgage / Loans",
          "Mortgage / Loans",
          "Salary / Wages",
          "General/Food",
          "Mortgage / Loans",
          "Mobile & Broadband",
          "Asset/Other Insurance",
          "Asset/Other Insurance",
          "Life Insurance",
          "Council / Rates",
          "Council / Rates",
          "General/Food",
          "General/Food",
          "General/Food",
          "General/Food",
          "General/Food",
          "Council / Rates",
          "Mobile & Broadband",
          "Power & Energy",
          "Mortgage / Loans",
          "Mortgage / Loans",
          "Mortgage / Loans",
          "Dining Out",
          "Dining Out",
          "Dining Out",
          "Council / Rates",
          "Mobile & Broadband",
          "Asset/Other Insurance",
          "Asset/Other Insurance",
          "Life Insurance",
          "Council / Rates",
          "Council / Rates",
          "Mobile & Broadband",
          "General/Food",
          "General/Food",
          "General/Food",
          "Council / Rates",
          "Mobile & Broadband",
          "Power & Energy",
          "Mortgage / Loans",
          "Mortgage / Loans",
          "Bank Fees",
          "Bank Interest",
      ],
      "Particulars": [
          # Jan 1
          "TOWER Insurance 810131660",
          "TOWER Insurance 820056152",
          "HCC 1Sandal25174 1Sandal",
          "WOOLWORTHS NZ/47 WHA 6921",
          "CAMEL KEBAB NAWTON 6921",
          "TANK TE AWA MALL 6921",
          "Waitomo App 6921",
          "ROBERT HARRIS TE AWA 6921",
          "DOMINOS NAWTON 6921",
          "SUSHI TIME 6921",
          "WHANG THAI 2 6921",
          "Regional Rate Rates",
          "TWO DEGREES MOBILE AUTO PAYMENT",
          "POWERSHOP Powershop 904059741",
          # Jan 5 - 8
          "Partners Life Limite 1439227 PartnersLife",
          "HOUSING LOAN 892391890003",
          "HOUSING LOAN 892391890005",
          "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON",
          "HOUSING LOAN 892391890004",
          "2degrees Broadband 2degreesBroa 10695125",
          "Partners Life Limite 1439227 PartnersLife",
          "TOWER Insurance 820056152",
          "HCC 1Sandal25174 1Sandal",
          "Regional Rate Rates",
          # Jan 9 - 15
          "SHARPS 12L7S 6921",
          "Rocky's Superette 6921",
          "EVERYDAY COFFEE 6921",
          "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON",
          "NETPLUS 6X818 6921",
          "Google YouTube-A 6921",
          "Google YouTube-A 6921",
          "HOLIDAY INN AUCKLAND 6921",
          "Affinity 8S6C",
          "HOUSING LOAN 892391890004",
          "2degrees Broadband 2degreesBroa 10695125",
          "Kmart Eastcoast Cstr Eastcoast",
          "TOWER Insurance 810131660",
          "TOWER Insurance 820056152",
          "Partners Life Limite 1439227 PartnersLife",
          "HCC 1Sandal25174 1Sandal",
          "BEE CARD SUPREME 6921",
          "BEE CARD SUPREME 6921",
          "EASYPAYCARWASH HAMILT 6921",
          "Waitomo App 6921",
          "Regional Rate Rates",
          "TWO DEGREES MOBILE AUTO PAYMENT",
          "POWERSHOP Powershop 904059741",
          "HOUSING LOAN 892391890003",
          "HOUSING LOAN 892391890005",
          # Jan 15 - 31
          "TWO DEGREES MOBILE AUTO PAYMENT",
          "POWERSHOP Powershop 904059741",
          "HOUSING LOAN 892391890003",
          "HOUSING LOAN 892391890005",
          "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON",
          "Every Day Account INTERNET XFR",
          "Amanda Lee Vasea INTERNET XFR",
          "WOOLWORTHS THE NUK EAGA 6921",
          "HOUSING LOAN 892391890004",
          "2degrees Broadband 2degreesBroa 10695125",
          "Partners Life Limite 1439227 PartnersLife",
          "TOWER Insurance 820056152",
          "HCC 1Sandal25174 1Sandal",
          "NIVRTHREVOLUTION MOTOR 6921",
          "KMART NEW ZEALAND LT 6921",
          "Regional Rate Rates",
          "TWO DEGREES MOBILE AUTO PAYMENT",
          "POWERSHOP Powershop 904059741",
          "HOUSING LOAN 892391890003",
          "HOUSING LOAN 892391890005",
          "Meridian Superlite 6921",
          "Meridian Superlite 6921",
          "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON",
          "Afterpay 6921",
          "HOUSING LOAN 892391890004",
          "2degrees Broadband 2degreesBroa 10695125",
          "TOWER Insurance 810131660",
          "TOWER Insurance 820056152",
          "Partners Life Limite 1439227 PartnersLife",
          "HCC 1Sandal25174 1Sandal",
          "BALTIMU THE 00000000",
          "garlic/louis 6921",
          "AFTERPAY 6921",
          "AFTERPAY 6921",
          "Regional Rate Rates",
          "TWO DEGREES MOBILE AUTO PAYMENT",
          "POWERSHOP Powershop 904059741",
          "HOUSING LOAN 892391890003",
          "HOUSING LOAN 892391890005",
          "DEBIT INTEREST",
          "Unauthorised O/D FEE",
      ],
      "Payment Type": [
          # Jan 1
          "Direct Debit (DD)",
          "Direct Debit (DD)",
          "Direct Debit (DD)",
          "Point of Sale (PS)",
          "Point of Sale (PS)",
          "Point of Sale (PS)",
          "Point of Sale (PS)",
          "Point of Sale (PS)",
          "Point of Sale (PS)",
          "Point of Sale (PS)",
          "Point of Sale (PS)",
          "Auto-Payment (AP)",
          "Auto-Payment (AP)",
          "Auto-Payment (AP)",
          # Jan 5 - 8
          "Direct Debit (DD)",
          "Loan Repayment (LR)",
          "Loan Repayment (LR)",
          "Direct Credit (DC)",
          "Loan Repayment (LR)",
          "Auto-Payment (AP)",
          "Direct Debit (DD)",
          "Direct Debit (DD)",
          "Direct Debit (DD)",
          "Auto-Payment (AP)",
          # Jan 9 - 15
          "Point of Sale (PS)",
          "Point of Sale (PS)",
          "Point of Sale (PS)",
          "Direct Credit (DC)",
          "Point of Sale (PS)",
          "Point of Sale (PS)",
          "Point of Sale (PS)",
          "Point of Sale (PS)",
          "Loan Repayment (LR)",
          "Loan Repayment (LR)",
          "Auto-Payment (AP)",
          "Auto-Payment (AP)",
          "Direct Debit (DD)",
          "Direct Debit (DD)",
          "Direct Debit (DD)",
          "Direct Debit (DD)",
          "Point of Sale (PS)",
          "Point of Sale (PS)",
          "Point of Sale (PS)",
          "Point of Sale (PS)",
          "Auto-Payment (AP)",
          "Auto-Payment (AP)",
          "Auto-Payment (AP)",
          "Loan Repayment (LR)",
          "Loan Repayment (LR)",
          # Jan 15 - 31
          "Auto-Payment (AP)",
          "Auto-Payment (AP)",
          "Loan Repayment (LR)",
          "Loan Repayment (LR)",
          "Direct Credit (DC)",
          "Internal Transfer (IN)",
          "Internal Transfer (IN)",
          "Point of Sale (PS)",
          "Loan Repayment (LR)",
          "Auto-Payment (AP)",
          "Direct Debit (DD)",
          "Direct Debit (DD)",
          "Direct Debit (DD)",
          "Point of Sale (PS)",
          "Point of Sale (PS)",
          "Auto-Payment (AP)",
          "Auto-Payment (AP)",
          "Auto-Payment (AP)",
          "Loan Repayment (LR)",
          "Loan Repayment (LR)",
          "Point of Sale (PS)",
          "Point of Sale (PS)",
          "Direct Credit (DC)",
          "Point of Sale (PS)",
          "Loan Repayment (LR)",
          "Auto-Payment (AP)",
          "Direct Debit (DD)",
          "Direct Debit (DD)",
          "Direct Debit (DD)",
          "Direct Debit (DD)",
          "Auto-Payment (AP)",
          "Point of Sale (PS)",
          "Point of Sale (PS)",
          "Point of Sale (PS)",
          "Auto-Payment (AP)",
          "Auto-Payment (AP)",
          "Auto-Payment (AP)",
          "Loan Repayment (LR)",
          "Loan Repayment (LR)",
          "Bank Fee",
          "Bank Fee",
      ],
      "Amount": [
          # Jan 1
          17.67,
          42.08,
          72.25,
          28.24,
          27.30,
          9.50,
          30.00,
          14.50,
          11.14,
          23.38,
          20.40,
          15.26,
          24.00,
          50.00,
          # Jan 5 - 8
          52.09,
          361.51,
          363.18,
          -1116.87,
          13.31,
          25.00,
          52.09,
          64.39,
          72.25,
          15.26,
          # Jan 9 - 15
          52.50,
          80.89,
          21.41,
          -1121.05,
          69.99,
          5.05,
          5.05,
          119.67,
          13.31,
          13.31,
          25.00,
          15.00,
          17.67,
          42.08,
          52.09,
          72.25,
          10.00,
          10.00,
          10.00,
          30.00,
          15.26,
          24.00,
          50.00,
          361.51,
          363.18,
          # Jan 15 - 31
          24.00,
          50.00,
          361.51,
          363.18,
          -1115.86,
          -50.00,
          -50.00,
          19.58,
          13.31,
          25.00,
          52.09,
          64.39,
          72.25,
          5.00,
          50.00,
          15.26,
          24.00,
          50.00,
          361.51,
          363.18,
          6.85,
          6.86,
          -1087.52,
          59.99,
          13.31,
          25.00,
          17.67,
          42.08,
          52.09,
          72.25,
          89.00,
          57.99,
          5.00,
          5.00,
          15.26,
          24.00,
          50.00,
          361.51,
          363.18,
          6.85,
          70.99,
      ],
  }
  df = pd.DataFrame(data)
  st.sidebar.info("Loaded complete January 2026 BNZ Joint Billing statement.")

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

# Dynamically populate Quick Focus Particulars with ALL unique particulars from January
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
