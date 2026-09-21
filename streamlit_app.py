import pandas as pd
import plotly.express as px
import streamlit as st

# Configure page layout
st.set_page_config(
    page_title="BNZ Joint Billing Dashboard (Income & Expenses)",
    page_icon="📊",
    layout="wide",
)

st.title(
    "📊 BNZ Joint Billing Account (02-0316-0685464-000) — Jan to Sep 2026"
)
st.markdown(
    "Complete itemized transaction ledger for **January through September"
    " 2026** with dedicated income tracking and monthly totals."
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
  # Complete dataset spanning January to September 2026 including monthly Affinity salary credits
  data = [
      # --- JANUARY ---
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
      # --- FEBRUARY ---
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
          "Date": "2026-02-06",
          "Month": "February",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Income",
          "Sub-Category": "Salary / Wages",
          "Particulars": "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON",
          "Payment Type": "Direct Credit (DC)",
          "Amount": -1116.87,
          "Budgeted Amount": 0.00,
      },
      # --- MARCH ---
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
          "Date": "2026-03-06",
          "Month": "March",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Income",
          "Sub-Category": "Salary / Wages",
          "Particulars": "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON",
          "Payment Type": "Direct Credit (DC)",
          "Amount": -1116.87,
          "Budgeted Amount": 0.00,
      },
      # --- APRIL ---
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
          "Date": "2026-04-06",
          "Month": "April",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Income",
          "Sub-Category": "Salary / Wages",
          "Particulars": "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON",
          "Payment Type": "Direct Credit (DC)",
          "Amount": -1116.87,
          "Budgeted Amount": 0.00,
      },
      # --- MAY ---
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
          "Date": "2026-05-06",
          "Month": "May",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Income",
          "Sub-Category": "Salary / Wages",
          "Particulars": "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON",
          "Payment Type": "Direct Credit (DC)",
          "Amount": -1116.87,
          "Budgeted Amount": 0.00,
      },
      # --- JUNE ---
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
          "Date": "2026-06-06",
          "Month": "June",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Income",
          "Sub-Category": "Salary / Wages",
          "Particulars": "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON",
          "Payment Type": "Direct Credit (DC)",
          "Amount": -1116.87,
          "Budgeted Amount": 0.00,
      },
      # --- JULY ---
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
          "Date": "2026-07-06",
          "Month": "July",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Income",
          "Sub-Category": "Salary / Wages",
          "Particulars": "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON",
          "Payment Type": "Direct Credit (DC)",
          "Amount": -1116.87,
          "Budgeted Amount": 0.00,
      },
      # --- AUGUST ---
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
          "Date": "2026-08-06",
          "Month": "August",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Income",
          "Sub-Category": "Salary / Wages",
          "Particulars": "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON",
          "Payment Type": "Direct Credit (DC)",
          "Amount": -1116.87,
          "Budgeted Amount": 0.00,
      },
      # --- SEPTEMBER ---
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
          "Date": "2026-09-06",
          "Month": "September",
          "Account Source": "BNZ Joint Billing Account",
          "Category": "Income",
          "Sub-Category": "Salary / Wages",
          "Particulars": "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON",
          "Payment Type": "Direct Credit (DC)",
          "Amount": -1116.87,
          "Budgeted Amount": 0.00,
      },
  ]
  df = pd.DataFrame(data)
  st.sidebar.info("Loaded complete Jan–Sep 2026 BNZ Joint Billing dataset.")

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

# Dynamically populate Quick Focus Particulars with ALL unique particulars
unique_particulars = sorted(df["Particulars"].dropna().unique().tolist())
focus_options = ["Show All Transactions"] + unique_particulars

selected_focus = st.sidebar.selectbox(
    "⚡ Quick Focus Particulars:", focus_options
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

# Calculate Total Actual vs Budgeted Spending (Outflows only)
total_actual_outflow = df_outflows["Amount"].sum()
total_budgeted_outflow = df_outflows["Budgeted Amount"].sum()

# Display KPI Summary Cards at the top
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

# Special Highlight if Affinity Salary is selected
if selected_focus == "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON":
  affinity_df = df[
      df["Particulars"]
      == "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON"
  ]
  total_affinity_income = abs(affinity_df["Amount"]).sum()
  st.success(
      f"💼 **Total Affinity Salary Inflows (Jan–Sep 2026):**"
      f" **${total_affinity_income:,.2f}** across {len(affinity_df)} months."
  )

st.markdown("---")

# Create Multi-Tabs
tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Visual Analytics",
    "📋 Detailed Ledger",
    "🏷️ Sub-Category & Budget Breakdown",
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
          df_filtered.groupby(["Month", "Particulars"])["Amount"]
          .apply(lambda x: abs(x.sum()))
          .reset_index()
      )
      fig_bar = px.bar(
          item_trend,
          x="Month",
          y="Amount",
          title=f"Monthly Trend for '{selected_focus}' (Jan - Sep)",
          text_auto="$",
      )
      st.plotly_chart(fig_bar, use_container_width=True)

with tab2:
  st.subheader("Statement Itemized Log (Joint Billing Account)")
  st.dataframe(df_filtered, use_container_width=True)

with tab3:
  st.subheader("Drill-Down by Sub-Category, Payment Type & Budget")
  if not df_outflows.empty:
    sub_summary = (
        df_outflows.groupby(
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
    sub_summary = sub_summary.rename(
        columns={"Amount": "Actual Amount", "Budgeted Amount": "Budgeted"}
    )
    sub_summary["Variance"] = (
        sub_summary["Budgeted"] - sub_summary["Actual Amount"]
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
