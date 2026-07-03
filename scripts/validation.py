import pandas as pd
from pathlib import Path

# Folder containing monthly CSVs
raw_data_folder = Path("data/raw_data")

# Read all CSV files
files = raw_data_folder.glob("*.csv")

df_list = []

for file in files:
    df = pd.read_csv(file)
    df_list.append(df)

sales = pd.concat(df_list, ignore_index=True)

# Validation checks
total_rows = len(sales)

# Null values
missing_customer_ids = sales["CustomerID"].isna().sum()

missing_descriptions = sales["Description"].isna().sum()

negative_quantities = (sales["Quantity"] < 0).sum()

negative_prices = (sales["UnitPrice"] < 0).sum()

# Duplicate values
duplicate_rows = sales.duplicated().sum()

c_invoices = sales["InvoiceNo"].astype(str).str.startswith("C").sum()

m_invoices = sales["InvoiceNo"].astype(str).str.startswith("M").sum()

report = f"""
VALIDATION REPORT
=================

Total Rows: {total_rows}

Missing Customer IDs: {missing_customer_ids}

Missing Descriptions: {missing_descriptions}

Negative Quantities: {negative_quantities}

Negative Prices: {negative_prices}

Duplicate Rows: {duplicate_rows}

Invoices Starting With C: {c_invoices}

Invoices Starting With M: {m_invoices}
"""

print(report)

report_path = Path("reports/validation_report.txt")

report_path.parent.mkdir(exist_ok=True)

with open(report_path, "w") as file:
    file.write(report)
