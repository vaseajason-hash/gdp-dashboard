import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="BNZ Joint Billing & Everyday Dashboard (2025-2026)",
    page_icon="📊",
    layout="wide",
)

st.title("📊 BNZ Financial Dashboard — Joint Billing & Everyday Account")
st.markdown(
    "Complete itemized transaction analytics featuring your **BNZ Joint"
    " Billing Account** and a separate dedicated section for your **Everyday"
    " Account**."
)

# ==========================================
# PART 1: BNZ JOINT BILLING ACCOUNT (PREVIOUS DATA & CHARTS)
# ==========================================
st.header("🏠 BNZ Joint Billing Account (02-0316-0685464-000)")

st.sidebar.header("📁 Joint Billing Data Source")
jb_uploaded_file = st.sidebar.file_uploader(
    "Upload CSV/Excel for Joint Billing Account",
    type=["csv", "xlsx", "xls"],
    key="jb_upload",
)

df_jb = None
if jb_uploaded_file is not None:
  try:
    if jb_uploaded_file.name.endswith(".csv"):
      df_jb = pd.read_csv(jb_uploaded_file)
    else:
      df_jb = pd.read_excel(jb_uploaded_file)
    st.sidebar.success("Joint Billing custom file loaded successfully!")
  except Exception as e:
    st.sidebar.error(f"Error reading file: {e}")

if df_jb is None:
  data_jb = [
      # JANUARY
      {
          "Date": "2026-01-01",
          "Month": "January",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Insurance",
          "Sub-Category": "Asset/Other Insurance",
          "Particulars": "TOWER Insurance 810131660",
          "Payment Type": "Direct Debit (DD)",
          "Amount": 17.67,
          "Budgeted Amount": 25.00,
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
          "Budgeted Amount": 72.25,
      },
      {
          "Date": "2026-01-10",
          "Month": "January",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Groceries",
          "Sub-Category": "Supermarket",
          "Particulars": "PAK'nSAVE Hamilton",
          "Payment Type": "Eftpos (EF)",
          "Amount": 245.80,
          "Budgeted Amount": 250.00,
      },
      {
          "Date": "2026-01-15",
          "Month": "January",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Dining & Entertainment",
          "Sub-Category": "Restaurants",
          "Particulars": "Whang Thai 2 Pad Thai",
          "Payment Type": "Visa Debit (VD)",
          "Amount": 48.50,
          "Budgeted Amount": 50.00,
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
          "Budgeted Amount": 0.00,
      },
      {
          "Date": "2026-01-13",
          "Month": "January",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Income",
          "Sub-Category": "Salary / Wages",
          "Particulars": "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON",
          "Payment Type": "Direct Credit (DC)",
          "Amount": -1121.05,
          "Budgeted Amount": 0.00,
      },
      {
          "Date": "2026-01-22",
          "Month": "January",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Income",
          "Sub-Category": "Salary / Wages",
          "Particulars": "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON",
          "Payment Type": "Direct Credit (DC)",
          "Amount": -1087.52,
          "Budgeted Amount": 0.00,
      },
      # FEBRUARY
      {
          "Date": "2026-02-01",
          "Month": "February",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Insurance",
          "Sub-Category": "Asset/Other Insurance",
          "Particulars": "TOWER Insurance 810131660",
          "Payment Type": "Direct Debit (DD)",
          "Amount": 17.67,
          "Budgeted Amount": 25.00,
      },
      {
          "Date": "2026-02-01",
          "Month": "February",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Housing",
          "Sub-Category": "Council / Rates",
          "Particulars": "HCC 1Sandal25174 1Sandal",
          "Payment Type": "Direct Debit (DD)",
          "Amount": 72.25,
          "Budgeted Amount": 72.25,
      },
      {
          "Date": "2026-02-05",
          "Month": "February",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Housing",
          "Sub-Category": "Mortgage / Loans",
          "Particulars": "HOUSING LOAN 892391890003",
          "Payment Type": "Loan Repayment (LR)",
          "Amount": 6145.24,
          "Budgeted Amount": 6145.24,
      },
      {
          "Date": "2026-02-08",
          "Month": "February",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Utilities",
          "Sub-Category": "Power & Energy",
          "Particulars": "POWERSHOP Powershop 904059741",
          "Payment Type": "Auto-Payment (AP)",
          "Amount": 175.00,
          "Budgeted Amount": 175.00,
      },
      {
          "Date": "2026-02-12",
          "Month": "February",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Groceries",
          "Sub-Category": "Supermarket",
          "Particulars": "Countdown Te Rapa",
          "Payment Type": "Eftpos (EF)",
          "Amount": 210.40,
          "Budgeted Amount": 220.00,
      },
      {
          "Date": "2026-02-03",
          "Month": "February",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Income",
          "Sub-Category": "Salary / Wages",
          "Particulars": "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON",
          "Payment Type": "Direct Credit (DC)",
          "Amount": -1116.87,
          "Budgeted Amount": 0.00,
      },
      {
          "Date": "2026-02-12",
          "Month": "February",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Income",
          "Sub-Category": "Salary / Wages",
          "Particulars": "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON",
          "Payment Type": "Direct Credit (DC)",
          "Amount": -1116.87,
          "Budgeted Amount": 0.00,
      },
      # MARCH
      {
          "Date": "2026-03-01",
          "Month": "March",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Insurance",
          "Sub-Category": "Asset/Other Insurance",
          "Particulars": "TOWER Insurance 810131660",
          "Payment Type": "Direct Debit (DD)",
          "Amount": 17.67,
          "Budgeted Amount": 25.00,
      },
      {
          "Date": "2026-03-01",
          "Month": "March",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Housing",
          "Sub-Category": "Council / Rates",
          "Particulars": "HCC 1Sandal25174 1Sandal",
          "Payment Type": "Direct Debit (DD)",
          "Amount": 72.25,
          "Budgeted Amount": 72.25,
      },
      {
          "Date": "2026-03-05",
          "Month": "March",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Housing",
          "Sub-Category": "Mortgage / Loans",
          "Particulars": "HOUSING LOAN 892391890003",
          "Payment Type": "Loan Repayment (LR)",
          "Amount": 6145.24,
          "Budgeted Amount": 6145.24,
      },
      {
          "Date": "2026-03-09",
          "Month": "March",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Utilities",
          "Sub-Category": "Power & Energy",
          "Particulars": "POWERSHOP Powershop 904059741",
          "Payment Type": "Auto-Payment (AP)",
          "Amount": 175.00,
          "Budgeted Amount": 175.00,
      },
      {
          "Date": "2026-03-14",
          "Month": "March",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Shopping",
          "Sub-Category": "Hardware / Tools",
          "Particulars": "Bunnings Warehouse Te Rapa",
          "Payment Type": "Visa Debit (VD)",
          "Amount": 134.90,
          "Budgeted Amount": 100.00,
      },
      {
          "Date": "2026-03-02",
          "Month": "March",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Income",
          "Sub-Category": "Salary / Wages",
          "Particulars": "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON",
          "Payment Type": "Direct Credit (DC)",
          "Amount": -1152.01,
          "Budgeted Amount": 0.00,
      },
      {
          "Date": "2026-03-10",
          "Month": "March",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Income",
          "Sub-Category": "Salary / Wages",
          "Particulars": "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON",
          "Payment Type": "Direct Credit (DC)",
          "Amount": -1097.12,
          "Budgeted Amount": 0.00,
      },
      {
          "Date": "2026-03-24",
          "Month": "March",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Income",
          "Sub-Category": "Salary / Wages",
          "Particulars": "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON",
          "Payment Type": "Direct Credit (DC)",
          "Amount": -1252.01,
          "Budgeted Amount": 0.00,
      },
      # APRIL
      {
          "Date": "2026-04-01",
          "Month": "April",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Insurance",
          "Sub-Category": "Asset/Other Insurance",
          "Particulars": "TOWER Insurance 810131660",
          "Payment Type": "Direct Debit (DD)",
          "Amount": 17.67,
          "Budgeted Amount": 25.00,
      },
      {
          "Date": "2026-04-01",
          "Month": "April",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Housing",
          "Sub-Category": "Council / Rates",
          "Particulars": "HCC 1Sandal25174 1Sandal",
          "Payment Type": "Direct Debit (DD)",
          "Amount": 72.25,
          "Budgeted Amount": 72.25,
      },
      {
          "Date": "2026-04-02",
          "Month": "April",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Housing",
          "Sub-Category": "Mortgage / Loans",
          "Particulars": "HOUSING LOAN 892391890003",
          "Payment Type": "Loan Repayment (LR)",
          "Amount": 6145.24,
          "Budgeted Amount": 6145.24,
      },
      {
          "Date": "2026-04-18",
          "Month": "April",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Groceries",
          "Sub-Category": "Supermarket",
          "Particulars": "The Warehouse Dinsdale",
          "Payment Type": "Visa Debit (VD)",
          "Amount": 88.30,
          "Budgeted Amount": 90.00,
      },
      {
          "Date": "2026-04-07",
          "Month": "April",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Income",
          "Sub-Category": "Salary / Wages",
          "Particulars": "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON",
          "Payment Type": "Direct Credit (DC)",
          "Amount": -1150.95,
          "Budgeted Amount": 0.00,
      },
      {
          "Date": "2026-04-21",
          "Month": "April",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Income",
          "Sub-Category": "Salary / Wages",
          "Particulars": "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON",
          "Payment Type": "Direct Credit (DC)",
          "Amount": -1170.59,
          "Budgeted Amount": 0.00,
      },
      # MAY
      {
          "Date": "2026-05-01",
          "Month": "May",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Insurance",
          "Sub-Category": "Asset/Other Insurance",
          "Particulars": "TOWER Insurance 810131660",
          "Payment Type": "Direct Debit (DD)",
          "Amount": 17.67,
          "Budgeted Amount": 25.00,
      },
      {
          "Date": "2026-05-01",
          "Month": "May",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Housing",
          "Sub-Category": "Council / Rates",
          "Particulars": "HCC 1Sandal25174 1Sandal",
          "Payment Type": "Direct Debit (DD)",
          "Amount": 72.25,
          "Budgeted Amount": 72.25,
      },
      {
          "Date": "2026-05-04",
          "Month": "May",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Housing",
          "Sub-Category": "Mortgage / Loans",
          "Particulars": "HOUSING LOAN 892391890003",
          "Payment Type": "Loan Repayment (LR)",
          "Amount": 6145.24,
          "Budgeted Amount": 6145.24,
      },
      {
          "Date": "2026-05-12",
          "Month": "May",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Health & Fitness",
          "Sub-Category": "Supplements",
          "Particulars": "Sprint Fit Online",
          "Payment Type": "Visa Debit (VD)",
          "Amount": 125.00,
          "Budgeted Amount": 120.00,
      },
      {
          "Date": "2026-05-05",
          "Month": "May",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Income",
          "Sub-Category": "Salary / Wages",
          "Particulars": "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON",
          "Payment Type": "Direct Credit (DC)",
          "Amount": -1200.00,
          "Budgeted Amount": 0.00,
      },
      {
          "Date": "2026-05-19",
          "Month": "May",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Income",
          "Sub-Category": "Salary / Wages",
          "Particulars": "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON",
          "Payment Type": "Direct Credit (DC)",
          "Amount": -1136.87,
          "Budgeted Amount": 0.00,
      },
      # JUNE
      {
          "Date": "2026-06-01",
          "Month": "June",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Insurance",
          "Sub-Category": "Asset/Other Insurance",
          "Particulars": "TOWER Insurance 810131660",
          "Payment Type": "Direct Debit (DD)",
          "Amount": 17.67,
          "Budgeted Amount": 25.00,
      },
      {
          "Date": "2026-06-03",
          "Month": "June",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Housing",
          "Sub-Category": "Lump-Sum Principal",
          "Particulars": "Extra Principal Transfer",
          "Payment Type": "Bank Transfer",
          "Amount": 30851.24,
          "Budgeted Amount": 0.00,
      },
      {
          "Date": "2026-06-03",
          "Month": "June",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Housing",
          "Sub-Category": "Mortgage / Loans",
          "Particulars": "HOUSING LOAN 892391890003",
          "Payment Type": "Loan Repayment (LR)",
          "Amount": 6145.24,
          "Budgeted Amount": 6145.24,
      },
      {
          "Date": "2026-06-20",
          "Month": "June",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Shopping",
          "Sub-Category": "Electronics",
          "Particulars": "PB Tech Hamilton",
          "Payment Type": "Visa Debit (VD)",
          "Amount": 450.00,
          "Budgeted Amount": 300.00,
      },
      {
          "Date": "2026-06-05",
          "Month": "June",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Income",
          "Sub-Category": "Salary / Wages",
          "Particulars": "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON",
          "Payment Type": "Direct Credit (DC)",
          "Amount": -1095.62,
          "Budgeted Amount": 0.00,
      },
      {
          "Date": "2026-06-16",
          "Month": "June",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Income",
          "Sub-Category": "Salary / Wages",
          "Particulars": "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON",
          "Payment Type": "Direct Credit (DC)",
          "Amount": -1200.00,
          "Budgeted Amount": 0.00,
      },
      # JULY
      {
          "Date": "2026-07-01",
          "Month": "July",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Insurance",
          "Sub-Category": "Asset/Other Insurance",
          "Particulars": "TOWER Insurance 810131660",
          "Payment Type": "Direct Debit (DD)",
          "Amount": 17.67,
          "Budgeted Amount": 25.00,
      },
      {
          "Date": "2026-07-01",
          "Month": "July",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Housing",
          "Sub-Category": "Council / Rates",
          "Particulars": "HCC 1Sandal25174 1Sandal",
          "Payment Type": "Direct Debit (DD)",
          "Amount": 72.25,
          "Budgeted Amount": 72.25,
      },
      {
          "Date": "2026-07-06",
          "Month": "July",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Housing",
          "Sub-Category": "Mortgage / Loans",
          "Particulars": "HOUSING LOAN 892391890003",
          "Payment Type": "Loan Repayment (LR)",
          "Amount": 6145.24,
          "Budgeted Amount": 6145.24,
      },
      {
          "Date": "2026-07-14",
          "Month": "July",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Dining & Entertainment",
          "Sub-Category": "Takeaways",
          "Particulars": "Thai Aroma Hamilton",
          "Payment Type": "Visa Debit (VD)",
          "Amount": 65.00,
          "Budgeted Amount": 60.00,
      },
      {
          "Date": "2026-07-07",
          "Month": "July",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Income",
          "Sub-Category": "Salary / Wages",
          "Particulars": "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON",
          "Payment Type": "Direct Credit (DC)",
          "Amount": -1165.67,
          "Budgeted Amount": 0.00,
      },
      {
          "Date": "2026-07-21",
          "Month": "July",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Income",
          "Sub-Category": "Salary / Wages",
          "Particulars": "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON",
          "Payment Type": "Direct Credit (DC)",
          "Amount": -1167.95,
          "Budgeted Amount": 0.00,
      },
      # AUGUST
      {
          "Date": "2026-08-01",
          "Month": "August",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Insurance",
          "Sub-Category": "Asset/Other Insurance",
          "Particulars": "TOWER Insurance 810131660",
          "Payment Type": "Direct Debit (DD)",
          "Amount": 17.67,
          "Budgeted Amount": 25.00,
      },
      {
          "Date": "2026-08-01",
          "Month": "August",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Housing",
          "Sub-Category": "Council / Rates",
          "Particulars": "HCC 1Sandal25174 1Sandal",
          "Payment Type": "Direct Debit (DD)",
          "Amount": 72.25,
          "Budgeted Amount": 72.25,
      },
      {
          "Date": "2026-08-04",
          "Month": "August",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Housing",
          "Sub-Category": "Mortgage / Loans",
          "Particulars": "HOUSING LOAN 892391890003",
          "Payment Type": "Loan Repayment (LR)",
          "Amount": 6145.24,
          "Budgeted Amount": 6145.24,
      },
      {
          "Date": "2026-08-11",
          "Month": "August",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Shopping",
          "Sub-Category": "DIY & Tools",
          "Particulars": "Purpose Fill Skip Bin Hire",
          "Payment Type": "Visa Debit (VD)",
          "Amount": 280.00,
          "Budgeted Amount": 250.00,
      },
      {
          "Date": "2026-08-04",
          "Month": "August",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Income",
          "Sub-Category": "Salary / Wages",
          "Particulars": "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON",
          "Payment Type": "Direct Credit (DC)",
          "Amount": -1182.87,
          "Budgeted Amount": 0.00,
      },
      {
          "Date": "2026-08-18",
          "Month": "August",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Income",
          "Sub-Category": "Salary / Wages",
          "Particulars": "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON",
          "Payment Type": "Direct Credit (DC)",
          "Amount": -1118.05,
          "Budgeted Amount": 0.00,
      },
      # SEPTEMBER
      {
          "Date": "2026-09-01",
          "Month": "September",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Insurance",
          "Sub-Category": "Asset/Other Insurance",
          "Particulars": "TOWER Insurance 810131660",
          "Payment Type": "Direct Debit (DD)",
          "Amount": 17.67,
          "Budgeted Amount": 25.00,
      },
      {
          "Date": "2026-09-01",
          "Month": "September",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Housing",
          "Sub-Category": "Council / Rates",
          "Particulars": "HCC 1Sandal25174 1Sandal",
          "Payment Type": "Direct Debit (DD)",
          "Amount": 72.25,
          "Budgeted Amount": 72.25,
      },
      {
          "Date": "2026-09-02",
          "Month": "September",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Housing",
          "Sub-Category": "Mortgage / Loans",
          "Particulars": "HOUSING LOAN 892391890003",
          "Payment Type": "Loan Repayment (LR)",
          "Amount": 6145.24,
          "Budgeted Amount": 6145.24,
      },
      {
          "Date": "2026-09-10",
          "Month": "September",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Dining & Entertainment",
          "Sub-Category": "Restaurants",
          "Particulars": "Whang Thai 2 Tom Yum",
          "Payment Type": "Visa Debit (VD)",
          "Amount": 54.00,
          "Budgeted Amount": 50.00,
      },
      {
          "Date": "2026-09-03",
          "Month": "September",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Income",
          "Sub-Category": "Salary / Wages",
          "Particulars": "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON",
          "Payment Type": "Direct Credit (DC)",
          "Amount": -1150.00,
          "Budgeted Amount": 0.00,
      },
      {
          "Date": "2026-09-17",
          "Month": "September",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Income",
          "Sub-Category": "Salary / Wages",
          "Particulars": "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON",
          "Payment Type": "Direct Credit (DC)",
          "Amount": -1100.00,
          "Budgeted Amount": 0.00,
      },
  ]
  df_jb = pd.DataFrame(data_jb)

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
if df_jb["Month"].dtype.name != "category":
  df_jb["Month"] = pd.Categorical(
      df_jb["Month"],
      categories=[
          m for m in month_order if m in df_jb["Month"].unique() or m == "January"
      ],
      ordered=True,
  )

df_jb = df_jb.sort_values("Month")

jb_col1, jb_col2 = st.columns(2)
jb_month = jb_col1.selectbox(
    "Filter Joint Billing Month:", ["All Months (Overview)"] + month_order, key="jb_m"
)
jb_particulars = jb_col2.selectbox(
    "Focus Joint Billing Particulars:",
    ["Show All Transactions"]
    + sorted(df_jb["Particulars"].dropna().unique().tolist()),
    key="jb_p",
)

df_jb_filtered = df_jb.copy()
if jb_month != "All Months (Overview)":
  df_jb_filtered = df_jb_filtered[df_jb_filtered["Month"] == jb_month]
if jb_particulars != "Show All Transactions":
  df_jb_filtered = df_jb_filtered[
      df_jb_filtered["Particulars"] == jb_particulars
  ]

df_jb_outflows = df_jb_filtered[df_jb_filtered["Category"] != "Income"]
jb_actual = df_jb_outflows["Amount"].sum()
jb_budget = df_jb_outflows["Budgeted Amount"].sum()

mk1, mk2, mk3 = st.columns(3)
mk1.metric(label="💵 Joint Billing Actual Spend", value=f"${jb_actual:,.2f}")
mk2.metric(label="📋 Joint Billing Budgeted", value=f"${jb_budget:,.2f}")
jb_var = jb_budget - jb_actual
mk3.metric(
    label="⚖️ Variance",
    value=f"${jb_var:,.2f}",
    delta=(
        f"${jb_var:,.2f} Under Budget"
        if jb_var >= 0
        else f"${abs(jb_var):,.2f} Over Budget"
    ),
)

tab_jb1, tab_jb2, tab_jb3 = st.tabs([
    "📈 Visual Analytics (Joint Billing)",
    "📋 Ledger (Joint Billing)",
    "🏷️ Budget Breakdown",
])

with tab_jb1:
  c1, c2 = st.columns(2)
  with c1:
    cat_sum_jb = (
        df_jb_outflows.groupby("Category")["Amount"].sum().reset_index()
    )
    fig_jb_pie = px.pie(
        cat_sum_jb,
        names="Category",
        values="Amount",
        hole=0.4,
        title="Joint Billing Outflows by Category",
    )
    st.plotly_chart(fig_jb_pie, use_container_width=True)
  with c2:
    if jb_month == "All Months (Overview)":
      monthly_jb = (
          df_jb_outflows.groupby(["Month", "Category"], observed=False)["Amount"]
          .sum()
          .reset_index()
      )
      fig_jb_bar = px.bar(
          monthly_jb,
          x="Month",
          y="Amount",
          color="Category",
          title="Total Outflows by Month & Category (Joint Billing)",
          barmode="stack",
          text_auto="$",
      )
      st.plotly_chart(fig_jb_bar, use_container_width=True)

  st.markdown("---")
  st.subheader(
      "🔍 Joint Billing Other Expenses (Excl. Housing, Insurance, Utilities)"
  )
  df_jb_other = df_jb_outflows[
      ~df_jb_outflows["Category"].isin(["Housing", "Insurance", "Utilities"])
  ]
  if not df_jb_other.empty:
    monthly_jb_other = (
        df_jb_other.groupby(["Month", "Category"], observed=False)["Amount"]
        .sum()
        .reset_index()
    )
    fig_jb_other = px.bar(
        monthly_jb_other,
        x="Month",
        y="Amount",
        color="Category",
        title="Other Expenses (Joint Billing)",
        barmode="stack",
        text_auto="$",
    )
    st.plotly_chart(fig_jb_other, use_container_width=True)

with tab_jb2:
  st.dataframe(df_jb_filtered, use_container_width=True)

with tab_jb3:
  if not df_jb_outflows.empty:
    sub_sum_jb = (
        df_jb_outflows.groupby(
            [
                "Month",
                "Category",
                "Sub-Category",
                "Payment Type",
                "Budgeted Amount",
            ]
        )["Amount"]
        .sum()
        .reset_index()
    )
    sub_sum_jb = sub_sum_jb.rename(
        columns={"Amount": "Actual Amount", "Budgeted Amount": "Budget"}
    )
    sub_sum_jb["Variance"] = sub_sum_jb["Budget"] - sub_sum_jb["Actual Amount"]
    st.dataframe(sub_sum_jb, use_container_width=True)

st.markdown("---")
st.markdown("---")

# ==========================================
# PART 2: EVERYDAY ACCOUNT (NEW SEPARATE SECTION)
# ==========================================
st.header("💳 Everyday Account (Separate Transactions)")

st.sidebar.markdown("---")
st.sidebar.header("📁 Everyday Account Data Source")
ev_uploaded_file = st.sidebar.file_uploader(
    "Upload CSV/Excel for Everyday Account",
    type=["csv", "xlsx", "xls"],
    key="ev_upload",
)

df_ev = None
if ev_uploaded_file is not None:
  try:
    if ev_uploaded_file.name.endswith(".csv"):
      df_ev = pd.read_csv(ev_uploaded_file)
    else:
      df_ev = pd.read_excel(ev_uploaded_file)
    st.sidebar.success("Everyday Account custom file loaded successfully!")
  except Exception as e:
    st.sidebar.error(f"Error reading file: {e}")

if df_ev is None:
  # Default sample data for Everyday Account based on user's recent statement export
  data_ev = [
      {
          "Date": "2025-09-24",
          "Month": "September",
          "Payee": "Amanda Lee Vasea",
          "Particulars": "INTERNET XFR",
          "Tran Type": "FT",
          "Amount": 70.00,
          "Category": "Transfers",
      },
      {
          "Date": "2025-09-25",
          "Month": "September",
          "Payee": "Pet N Sur",
          "Particulars": "PetnSur Astro",
          "Tran Type": "DD",
          "Amount": -28.16,
          "Category": "Insurance",
      },
      {
          "Date": "2025-09-26",
          "Month": "September",
          "Payee": "GOCARDLESS",
          "Particulars": "IRONHOUSEGYM",
          "Tran Type": "DD",
          "Amount": -20.00,
          "Category": "Health & Fitness",
      },
      {
          "Date": "2025-09-26",
          "Month": "September",
          "Payee": "AMANDA VASEA",
          "Particulars": "DISHONOUR-03",
          "Tran Type": "DC",
          "Amount": 52.00,
          "Category": "Income",
      },
      {
          "Date": "2025-10-03",
          "Month": "October",
          "Payee": "GOCARDLESS",
          "Particulars": "IRONHOUSEGYM",
          "Tran Type": "DD",
          "Amount": -20.00,
          "Category": "Health & Fitness",
      },
      {
          "Date": "2025-10-08",
          "Month": "October",
          "Payee": "Amanda Lee Vasea",
          "Particulars": "INTERNET XFR",
          "Tran Type": "FT",
          "Amount": 70.00,
          "Category": "Transfers",
      },
  ]
  df_ev = pd.DataFrame(data_ev)

# Standardize Everyday Account columns if uploaded from raw bank CSV
if "Date" in df_ev.columns and "Month" not in df_ev.columns:
  df_ev["Date_Parsed"] = pd.to_datetime(
      df_ev["Date"], format="%d/%m/%Y", errors="coerce"
  )
  if df_ev["Date_Parsed"].isna().all():
    df_ev["Date_Parsed"] = pd.to_datetime(df_ev["Date"], errors="coerce")
  df_ev["Month"] = df_ev["Date_Parsed"].dt.month_name()

if "Category" not in df_ev.columns:
  df_ev["Category"] = "General"
if "Amount" not in df_ev.columns:
  df_ev["Amount"] = 0.0

ev_col1, ev_col2 = st.columns(2)
available_ev_months = [
    m
    for m in [
        "September",
        "October",
        "November",
        "December",
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
    if m in df_ev["Month"].dropna().unique()
]
ev_month = ev_col1.selectbox(
    "Filter Everyday Account Month:",
    ["All Months (Overview)"] + available_ev_months,
    key="ev_m",
)
ev_particulars = ev_col2.selectbox(
    "Focus Everyday Account Particulars/Payee:",
    ["Show All Transactions"]
    + sorted(
        df_ev["Particulars"].dropna().unique().tolist()
        if "Particulars" in df_ev.columns
        else []
    ),
    key="ev_p",
)

df_ev_filtered = df_ev.copy()
if ev_month != "All Months (Overview)":
  df_ev_filtered = df_ev_filtered[df_ev_filtered["Month"] == ev_month]
if ev_particulars != "Show All Transactions":
  df_ev_filtered = df_ev_filtered[df_ev_filtered["Particulars"] == ev_particulars]

ev_total = df_ev_filtered["Amount"].sum()

ek1, ek2 = st.columns(2)
ek1.metric(
    label="💳 Everyday Account Net Total (Filtered)", value=f"${ev_total:,.2f}"
)
ek2.metric(label="📑 Total Everyday Transactions", value=len(df_ev_filtered))

tab_ev1, tab_ev2 = st.tabs([
    "📈 Visual Analytics (Everyday Account)",
    "📋 Ledger (Everyday Account)",
])

with tab_ev1:
  if not df_ev_filtered.empty and "Category" in df_ev_filtered.columns:
    fig_ev_pie = px.pie(
        df_ev_filtered,
        names="Category",
        values="Amount",
        hole=0.4,
        title="Everyday Account Breakdown by Category",
    )
    st.plotly_chart(fig_ev_pie, use_container_width=True)
  else:
    st.info("No data available for Everyday Account visualization.")

with tab_ev2:
  st.dataframe(df_ev_filtered, use_container_width=True)
