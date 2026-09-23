import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="BNZ Joint Billing Dashboard (Jan-Sep 2026)",
    page_icon="📊",
    layout="wide",
)

st.title(
    "📊 BNZ Joint Billing Account (02-0316-0685464-000) — Jan to Sep 2026"
)
st.markdown(
    "Complete itemized transaction ledger with automatic BNZ statement parsing,"
    " stacked monthly expenses, and non-housing/insurance breakdown."
)

# --- CSV / EXCEL FILE UPLOADER IN SIDEBAR ---
st.sidebar.header("📁 Data Source & File Upload")
uploaded_file = st.sidebar.file_uploader(
    "Drop or upload your CSV / Excel statement", type=["csv", "xlsx", "xls"]
)

df = None

if uploaded_file is not None:
  try:
    if uploaded_file.name.endswith(".csv"):
      df = pd.read_csv(uploaded_file)
    else:
      xls = pd.ExcelFile(uploaded_file)
      sheet_to_load = xls.sheet_names[0]
      df = pd.read_excel(uploaded_file, sheet_name=sheet_to_load)

    st.sidebar.success(f"Successfully loaded '{uploaded_file.name}'!")

    # AUTOMATIC BNZ COLUMN MAPPING ADAPTER
    # Maps raw BNZ export headers to dashboard structure
    if "Payee" in df.columns and "Particulars" in df.columns:
      df["Month"] = pd.to_datetime(df["Date"], errors="coerce").dt.month_name()
      # Categorize based on Payee / Particulars keywords
      def auto_categorize(row):
        text = str(row["Payee"]) + " " + str(row["Particulars"])
        if "AFFINITY" in text.upper():
          return "Income"
        elif "TOWER" in text.upper() or "INSURANCE" in text.upper():
          return "Insurance"
        elif "HCC" in text.upper() or "HOUSING" in text.upper():
          return "Housing"
        elif "POWERSHOP" in text.upper():
          return "Utilities"
        elif "PAK'NSAVE" in text.upper() or "COUNTDOWN" in text.upper():
          return "Groceries"
        else:
          return "General / Shopping"

      df["Category"] = df.apply(auto_categorize, axis=1)
      df["Sub-Category"] = df["Payee"]
      df["Budgeted Amount"] = 0.0

  except Exception as e:
    st.sidebar.error(f"Error reading uploaded file: {e}")

# Fallback to built-in sample dataset if no file uploaded
if df is None:
  st.sidebar.info("Using built-in sample dataset. Upload your Excel file above.")
  data = [
      {
          "Date": "2026-01-01",
          "Month": "January",
          "Category": "Insurance",
          "Sub-Category": "TOWER Insurance",
          "Particulars": "TOWER Insurance",
          "Amount": 17.67,
          "Budgeted Amount": 25.00,
      },
      {
          "Date": "2026-01-06",
          "Month": "January",
          "Category": "Income",
          "Sub-Category": "Salary",
          "Particulars": "AFFINITY EMPL GWF PAY",
          "Amount": -1116.87,
          "Budgeted Amount": 0.00,
      },
      {
          "Date": "2026-02-05",
          "Month": "February",
          "Category": "Housing",
          "Sub-Category": "Mortgage",
          "Particulars": "HOUSING LOAN",
          "Amount": 6145.24,
          "Budgeted Amount": 6145.24,
      },
  ]
  df = pd.DataFrame(data)

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
if "Month" in df.columns:
  df["Month"] = pd.Categorical(
      df["Month"],
      categories=[m for m in month_order if m in df["Month"].unique() or True],
      ordered=True,
  )

# Sidebar Filters
st.sidebar.markdown("---")
selected_month = st.sidebar.selectbox(
    "Select Month:", ["All Months (Overview)"] + month_order
)

unique_particulars = (
    sorted(df["Particulars"].dropna().unique().tolist())
    if "Particulars" in df.columns
    else []
)
focus_options = ["Show All Transactions"] + unique_particulars
selected_focus = st.sidebar.selectbox(
    "⚡ Quick Focus Particulars:", focus_options
)

# Apply filters
df_filtered = df.copy()

if (
    selected_month != "All Months (Overview)"
    and "Month" in df_filtered.columns
):
  df_filtered = df_filtered[df_filtered["Month"] == selected_month]

if selected_focus != "Show All Transactions":
  df_filtered = df_filtered[df_filtered["Particulars"] == selected_focus]

st.subheader(
    f"📅 Viewing: {selected_month} | Focus: {selected_focus}"
    if selected_focus != "Show All Transactions"
    else f"📅 Viewing: {selected_month}"
)

df_outflows = df_filtered[df_filtered["Category"] != "Income"]
total_actual_outflow = (
    df_outflows["Amount"].sum() if "Amount" in df_outflows.columns else 0.0
)
total_budgeted_outflow = (
    df_outflows["Budgeted Amount"].sum()
    if "Budgeted Amount" in df_outflows.columns
    else 0.0
)

kpi1, kpi2, kpi3 = st.columns(3)
kpi1.metric(
    label="💵 Total Actual Spending", value=f"${total_actual_outflow:,.2f}"
)
kpi2.metric(
    label="📋 Total Budgeted Spending", value=f"${total_budgeted_outflow:,.2f}"
)
variance = total_budgeted_outflow - total_actual_outflow
kpi3.metric(
    label="⚖️ Budget Variance",
    value=f"${variance:,.2f}",
    delta=(
        f"${variance:,.2f} Under Budget"
        if variance >= 0
        else f"${abs(variance):,.2f} Over Budget"
    ),
)

st.markdown("---")

tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Visual Analytics",
    "📋 Detailed Ledger",
    "🏷️ Sub-Category & Budget Breakdown",
    "🔍 Search & Filter",
])

with tab1:
  col1, col2 = st.columns(2)
  with col1:
    if not df_outflows.empty and "Category" in df_outflows.columns:
      cat_summary = (
          df_outflows.groupby("Category")["Amount"].sum().reset_index()
      )
      fig_donut = px.pie(
          cat_summary,
          names="Category",
          values="Amount",
          hole=0.4,
          title="Outflows by Main Category",
      )
      st.plotly_chart(fig_donut, use_container_width=True)
  with col2:
    if selected_focus == "Show All Transactions" and "Month" in df_outflows.columns:
      if selected_month == "All Months (Overview)":
        monthly_cat_summary = (
            df_outflows.groupby(["Month", "Category"], observed=False)["Amount"]
            .sum()
            .reset_index()
        )
        fig_bar = px.bar(
            monthly_cat_summary,
            x="Month",
            y="Amount",
            color="Category",
            title="Total Outflows by Month & Category (All Expenses)",
            text_auto="$",
            barmode="stack",
        )
        st.plotly_chart(fig_bar, use_container_width=True)

  st.markdown("---")
  st.subheader(
      "🔍 Secondary Breakdown: Other Expenses (Excluding Housing, Insurance &"
      " Utilities)"
  )
  excluded_categories = ["Housing", "Insurance", "Utilities"]
  if not df_outflows.empty and "Category" in df_outflows.columns:
    df_other_expenses = df_outflows[
        ~df_outflows["Category"].isin(excluded_categories)
    ]
    if not df_other_expenses.empty:
      other_monthly_summary = (
          df_other_expenses.groupby(["Month", "Category"], observed=False)[
              "Amount"
          ]
          .sum()
          .reset_index()
      )
      fig_bar_other = px.bar(
          other_monthly_summary,
          x="Month",
          y="Amount",
          color="Category",
          title=(
              "Other Expenses by Month & Category (Excl. Housing, Insurance,"
              " Utilities)"
          ),
          text_auto="$",
          barmode="stack",
      )
      st.plotly_chart(fig_bar_other, use_container_width=True)
    else:
      st.info("No other expenses found outside excluded categories.")

with tab2:
  st.dataframe(df_filtered, use_container_width=True)

with tab3:
  if not df_outflows.empty:
    st.dataframe(df_outflows, use_container_width=True)
  else:
    st.info("No matching outflow data.")

with tab4:
  search_term = st.text_input("Filter by custom keyword")
  if search_term and not df_filtered.empty:
    text_cols = df_filtered.select_dtypes(include=["object"]).columns
    mask = df_filtered[text_cols].apply(
        lambda col: col.str.contains(search_term, case=False, na=False)
    ).any(axis=1)
    st.dataframe(df_filtered[mask], use_container_width=True)
