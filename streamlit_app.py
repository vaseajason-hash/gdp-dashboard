import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="BNZ Accounts Dashboard (2025-2026)",
    page_icon="📊",
    layout="wide",
)

st.title("📊 BNZ Financial Dashboard — Joint Billing vs. Everyday Account")
st.markdown(
    "Manage and analyze transactions separately across your **BNZ Joint Billing"
    " Account** and your **Everyday Account** (Sept 2025 - Sept 2026)."
)

# --- SIDEBAR ACCOUNT & FILE MANGER ---
st.sidebar.header("📁 Account & File Manager")
account_selection = st.sidebar.selectbox(
    "Select Active Account:",
    ["BNZ Joint Billing Account", "Everyday Account"],
)

uploaded_file = st.sidebar.file_uploader(
    f"Upload CSV/Excel statement for {account_selection}",
    type=["csv", "xlsx", "xls"],
)

df = None

if uploaded_file is not None:
  try:
    if uploaded_file.name.endswith(".csv"):
      df = pd.read_csv(uploaded_file)
    else:
      xls = pd.ExcelFile(uploaded_file)
      df = pd.read_excel(uploaded_file, sheet_name=xls.sheet_names[0])
    st.sidebar.success(
        f"Successfully loaded '{uploaded_file.name}' for {account_selection}!"
    )
  except Exception as e:
    st.sidebar.error(f"Error reading file: {e}")

# Default sample data if no file uploaded for the selected account
if df is None:
  if account_selection == "Everyday Account":
    st.sidebar.info(
        "Using sample Everyday Account data. Drop in your Everyday Account CSV"
        " above."
    )
    data = [
        {
            "Date": "24/09/2025",
            "Payee": "Amanda Lee Vasea",
            "Particulars": "INTERNET XFR",
            "Tran Type": "FT",
            "Amount": 70.00,
            "Category": "Transfers",
        },
        {
            "Date": "25/09/2025",
            "Payee": "Pet N Sur",
            "Particulars": "PetnSur Astro",
            "Tran Type": "DD",
            "Amount": -28.16,
            "Category": "Insurance",
        },
        {
            "Date": "26/09/2025",
            "Payee": "GOCARDLESS",
            "Particulars": "IRONHOUSEGYM",
            "Tran Type": "DD",
            "Amount": -20.00,
            "Category": "Health & Fitness",
        },
        {
            "Date": "26/09/2025",
            "Payee": "AMANDA VASEA",
            "Particulars": "DISHONOUR-03",
            "Tran Type": "DC",
            "Amount": 52.00,
            "Category": "Income",
        },
    ]
    df = pd.DataFrame(data)
  else:
    st.sidebar.info("Using sample Joint Billing Account data.")
    data = [
        {
            "Date": "2026-01-01",
            "Payee": "TOWER Insurance",
            "Particulars": "Insurance",
            "Tran Type": "DD",
            "Amount": 17.67,
            "Category": "Insurance",
            "Budgeted Amount": 25.00,
        },
        {
            "Date": "2026-01-01",
            "Payee": "HCC Rates",
            "Particulars": "Rates",
            "Tran Type": "DD",
            "Amount": 72.25,
            "Category": "Housing",
            "Budgeted Amount": 72.25,
        },
        {
            "Date": "2026-01-06",
            "Payee": "AFFINITY EMPL",
            "Particulars": "GWF PAY",
            "Tran Type": "DC",
            "Amount": -1116.87,
            "Category": "Income",
            "Budgeted Amount": 0.00,
        },
    ]
    df = pd.DataFrame(data)

# Process Dates & Months
if "Date" in df.columns:
  # Handle both DD/MM/YYYY and YYYY-MM-DD formats automatically
  df["Date_Parsed"] = pd.to_datetime(df["Date"], errors="coerce")
  if df["Date_Parsed"].isna().all():
    df["Date_Parsed"] = pd.to_datetime(
        df["Date"], format="%d/%m/%Y", errors="coerce"
    )
  df["Month"] = df["Date_Parsed"].dt.month_name()

if "Category" not in df.columns:
  df["Category"] = "General"
if "Amount" not in df.columns:
  df["Amount"] = 0.0
if "Budgeted Amount" not in df.columns:
  df["Budgeted Amount"] = 0.0

st.sidebar.markdown("---")
month_order = [
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
valid_months = [m for m in month_order if m in df["Month"].dropna().unique()]
selected_month = st.sidebar.selectbox(
    "Select Month:",
    ["All Months (Overview)"] + valid_months
    if valid_months
    else ["All Months (Overview)"],
)

df_filtered = df.copy()
if (
    selected_month != "All Months (Overview)"
    and "Month" in df_filtered.columns
):
  df_filtered = df_filtered[df_filtered["Month"] == selected_month]

st.subheader(
    f"📂 Active Account: **{account_selection}** | Month: {selected_month}"
)

# KPIs
col1, col2 = st.columns(2)
total_amount = df_filtered["Amount"].sum()
col1.metric(label="📊 Total Net Amount (Filtered)", value=f"${total_amount:,.2f}")
col2.metric(label="📑 Total Transactions", value=len(df_filtered))

st.markdown("---")

tab1, tab2, tab3 = st.tabs(
    ["📋 Transaction Ledger", "📈 Visual Breakdown", "🔍 Search & Filter"]
)

with tab1:
  st.dataframe(df_filtered, use_container_width=True)

with tab2:
  if "Category" in df_filtered.columns and not df_filtered.empty:
    fig_pie = px.pie(
        df_filtered,
        names="Category",
        values="Amount",
        hole=0.4,
        title=f"Transactions by Category ({account_selection})",
    )
    st.plotly_chart(fig_pie, use_container_width=True)
  else:
    st.info("Insufficient category data for visualization.")

with tab3:
  search_term = st.text_input("Filter transactions by keyword")
  if search_term:
    text_cols = df_filtered.select_dtypes(include=["object"]).columns
    mask = df_filtered[text_cols].apply(
        lambda col: col.str.contains(search_term, case=False, na=False)
    ).any(axis=1)
    st.dataframe(df_filtered[mask], use_container_width=True)
