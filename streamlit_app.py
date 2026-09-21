import pandas as pd
import plotly.express as px
import streamlit as st

# Configure page layout
st.set_page_config(
    page_title="BNZ Joint Billing Dashboard", page_icon="📊", layout="wide"
)

st.title("📊 BNZ Joint Billing Account - Detailed Analytics")
st.markdown(
    "Itemized transaction tracking based on your bank statement, broken down"
    " by category, sub-category, and payment type."
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
  # Sample dataset matching the exact BNZ Statement snapshot
  data = {
      "Date": [
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
      ],
      "Month": ["January"] * 24,
      "Category": [
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
      ],
      "Sub-Category": [
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
      ],
      "Particulars": [
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
      ],
      "Payment Type": [
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
      ],
      "Amount": [
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
          52.09,
          361.51,
          363.18,
          -1116.87,  # Negative for deposit/inflow
          13.31,
          25.00,
          52.09,
          64.39,
          72.25,
          15.26,
      ],
  }
  df = pd.DataFrame(data)
  st.sidebar.info(
      "Loaded exact statement sample data with particulars & payment types."
  )

# Filter out income for outflow summaries
df_outflows = df[df["Category"] != "Income"]

# Create Multi-Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Visual Analytics",
    "📋 Detailed Ledger",
    "🏷️ Sub-Category Breakdown",
    "🔍 Search & Filter",
])

with tab1:
  st.subheader("Outflow Proportions & Breakdown")
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
    pay_summary = (
        df_outflows.groupby("Payment Type")["Amount"].sum().reset_index()
    )
    fig_pay = px.bar(
        pay_summary,
        x="Payment Type",
        y="Amount",
        title="Outflows by Payment Type (DD, PS, AP, LR)",
        text_auto="$",
    )
    st.plotly_chart(fig_pay, use_container_width=True)

with tab2:
  st.subheader("Complete Statement Itemized Log")
  st.dataframe(df, use_container_width=True)

with tab3:
  st.subheader("Drill-Down by Sub-Category & Payment Type")
  sub_summary = (
      df_outflows.groupby(["Category", "Sub-Category", "Payment Type"])["Amount"]
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
      "Filter by keyword (e.g., 'TOWER', 'Powershop', 'Direct Debit')"
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
    st.info(
        "Type a keyword above to look up specific particulars or payment"
        " types."
    )
