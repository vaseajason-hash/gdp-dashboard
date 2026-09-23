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
# PART 1: BNZ JOINT BILLING ACCOUNT (ISOLATED)
# ==========================================
st.header("🏠 BNZ Joint Billing Account (02-0316-0685464-000)")

st.sidebar.header("📁 Joint Billing Data Source")
jb_uploaded_file = st.sidebar.file_uploader(
    "Upload CSV/Excel for Joint Billing Account",
    type=["csv", "xlsx", "xls"],
    key="jb_file_uploader_unique",
)

df_jb = None
if jb_uploaded_file is not None:
  try:
    if jb_uploaded_file.name.endswith(".csv"):
      df_jb = pd.read_csv(jb_uploaded_file)
    else:
      df_jb = pd.read_excel(jb_uploaded_file)
    st.sidebar.success("Joint Billing file loaded successfully!")
  except Exception as e:
    st.sidebar.error(f"Error reading Joint Billing file: {e}")

if df_jb is None:
  data_jb = [
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
# PART 2: EVERYDAY ACCOUNT (ISOLATED)
# ==========================================
st.header("💳 Everyday Account (Separate Transactions)")

st.sidebar.markdown("---")
st.sidebar.header("📁 Everyday Account Data Source")
ev_uploaded_file = st.sidebar.file_uploader(
    "Upload CSV/Excel for Everyday Account",
    type=["csv", "xlsx", "xls"],
    key="ev_file_uploader_unique",
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
    st.sidebar.error(f"Error reading Everyday file: {e}")

if df_ev is None:
  data_ev = [
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
  df_ev = pd.DataFrame(data_ev)

# Standardize Everyday Account columns & parse dates
if "Date" in df_ev.columns:
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
    if "Month" in df_ev.columns and m in df_ev["Month"].dropna().unique()
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
if ev_month != "All Months (Overview)" and "Month" in df_ev_filtered.columns:
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
    "📋 Ledger & Transaction Table",
    "📈 Visual Analytics & All Transactions Graph",
])

with tab_ev1:
  st.dataframe(df_ev_filtered, use_container_width=True)

with tab_ev2:
  if not df_ev_filtered.empty:
    fig_ev_pie = px.pie(
        df_ev_filtered,
        names="Payee" if "Payee" in df_ev_filtered.columns else "Category",
        values="Amount",
        hole=0.4,
        title="Everyday Account Breakdown by Payee / Category",
    )
    st.plotly_chart(fig_ev_pie, use_container_width=True)

    st.markdown("---")
    st.subheader("📊 Everyday Account All Transactions Timeline")

    if "Date_Parsed" in df_ev_filtered.columns:
      df_sorted = df_ev_filtered.sort_values("Date_Parsed")
      fig_timeline = px.bar(
          df_sorted,
          x="Date_Parsed",
          y="Amount",
          color=(
              "Payee" if "Payee" in df_sorted.columns else "Tran Type"
          ),
          title="All Transactions over Time (Everyday Account)",
          hover_data=["Particulars", "Amount", "Tran Type"],
      )
      st.plotly_chart(fig_timeline, use_container_width=True)
  else:
    st.info("No data available for Everyday Account visualization.")
