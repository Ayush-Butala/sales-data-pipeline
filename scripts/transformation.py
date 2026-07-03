import pandas as pd
from pathlib import Path

input_file = Path("data/cleaned_data/clean_sales.csv")
output_file = Path("data/cleaned_data/analytics_sales.csv")

# Load data
sales = pd.read_csv(input_file)

print(f"Rows Loaded: {len(sales):,}")

# -----------------------------
# Type conversions
# -----------------------------
sales["InvoiceDate"] = pd.to_datetime(sales["InvoiceDate"], errors="coerce")

sales["Quantity"] = pd.to_numeric(sales["Quantity"], errors="coerce")
sales["UnitPrice"] = pd.to_numeric(sales["UnitPrice"], errors="coerce")

# -----------------------------
# Feature Engineering
# -----------------------------
sales["Revenue"] = (sales["Quantity"] * sales["UnitPrice"]).round(2)

sales["Year"] = sales["InvoiceDate"].dt.year
sales["Month"] = sales["InvoiceDate"].dt.month_name()
sales["MonthNumber"] = sales["InvoiceDate"].dt.month
sales["Quarter"] = "Q" + sales["InvoiceDate"].dt.quarter.astype(str)
sales["DayOfWeek"] = sales["InvoiceDate"].dt.day_name()

# -----------------------------
# FIXED: IsReturn (DO NOT use column that doesn't exist)
# -----------------------------
sales["IsReturn"] = (
    sales["InvoiceNo"]
    .astype(str)
    .str.startswith("C")
    .astype(int)
)

# Optional: Transaction Type (clean business feature)
sales["TransactionType"] = sales["IsReturn"].map({
    0: "Sale",
    1: "Return"
})

# -----------------------------
# Column ordering
# -----------------------------
column_order = [
    "InvoiceNo",
    "StockCode",
    "Description",
    "CustomerID",
    "Country",
    "InvoiceDate",
    "Year",
    "Quarter",
    "Month",
    "MonthNumber",
    "DayOfWeek",
    "Quantity",
    "UnitPrice",
    "Revenue",
    "TransactionType",
    "IsReturn"
]

sales = sales[column_order]

# -----------------------------
# Save output
# -----------------------------
sales.to_csv(output_file, index=False)

print("\nTransformation Complete!")
print(f"Rows: {len(sales):,}")
print(f"Columns: {len(sales.columns)}")
print(f"Saved To: {output_file}")