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
    "Complete itemized transaction ledger for **January through September"
    " 2026** with exact varying salary inflows and monthly spending/budget"
    " tracking."
)

data = [
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
df["Month"] = pd.Categorical(
    df["Month"], categories=month_order, ordered=True
)
df = df.sort_values("Month")

st.sidebar.header("📁 Filters")
selected_month = st.sidebar.selectbox(
    "Select Month:", ["All Months (Overview)"] + month_order
)
focus_options = ["Show All Transactions"] + sorted(
    df["Particulars"].dropna().unique().tolist()
)
selected_focus = st.sidebar.selectbox(
    "⚡ Quick Focus Particulars:", focus_options
)

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

df_outflows = df_filtered[df_filtered["Category"] != "Income"]
total_actual_outflow = df_outflows["Amount"].sum()
total_budgeted_outflow = df_outflows["Budgeted Amount"].sum()

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

if selected_focus == "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON":
  affinity_df = df[
      df["Particulars"]
      == "AFFINITY EMPL GWF PAY MAURI HAMILT VASEA. JASON"
  ]
  total_affinity_income = abs(affinity_df["Amount"]).sum()
  st.success(
      f"💼 **Total Affinity Salary Inflows (Jan–Sep 2026):**"
      f" **${total_affinity_income:,.2f}** across all months (exact varying pay"
      " amounts)."
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
          title=f"Monthly Total for '{selected_focus}' (Jan - Sep)",
          text_auto="$",
      )
      st.plotly_chart(fig_bar, use_container_width=True)

with tab2:
  st.dataframe(df_filtered, use_container_width=True)

with tab3:
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
  else:
    st.info("No matching outflow data.")

with tab4:
  search_term = st.text_input("Filter by custom keyword")
  if search_term:
    text_cols = df_filtered.select_dtypes(include=["object"]).columns
    mask = df_filtered[text_cols].apply(
        lambda col: col.str.contains(search_term, case=False, na=False)
    ).any(axis=1)
    st.dataframe(df_filtered[mask], use_container_width=True)
