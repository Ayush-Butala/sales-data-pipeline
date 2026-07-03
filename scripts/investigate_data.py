# For research only

import pandas as pd
from pathlib import Path

raw_data_folder = Path("data/raw_data")

files = raw_data_folder.glob("*.csv")

df_list = []

for file in files:
    df = pd.read_csv(file)
    df_list.append(df)

sales = pd.concat(df_list, ignore_index=True)

print("\n" + "=" * 60)
print("NEGATIVE PRICE ROWS")
print("=" * 60)

negative_price_rows = sales[sales["UnitPrice"] < 0]

print(negative_price_rows)

print("\nTotal Negative Price Rows:")
print(len(negative_price_rows))

print("\n" + "=" * 60)
print("MISSING DESCRIPTION ROWS (FIRST 10)")
print("=" * 60)

missing_description_rows = sales[
    sales["Description"].isna()
]

print(
    missing_description_rows[
        ["InvoiceNo", "StockCode", "Description"]
    ].head(10)
)

print("\nTotal Missing Descriptions:")
print(len(missing_description_rows))

print("\nUnique StockCodes With Missing Descriptions:")
print(
    missing_description_rows["StockCode"]
    .nunique()
)

print("\n" + "=" * 60)
print("MISSING CUSTOMER ID ROWS (FIRST 10)")
print("=" * 60)

missing_customer_rows = sales[
    sales["CustomerID"].isna()
]

print(
    missing_customer_rows.head(10)
)

print("\nTotal Missing Customer IDs:")
print(len(missing_customer_rows))

print("\n" + "=" * 60)
print("SAMPLE RETURN TRANSACTIONS")
print("=" * 60)

returns = sales[sales["Quantity"] < 0]

print(
    returns[
        [
            "InvoiceNo",
            "Quantity",
            "Description",
            "UnitPrice"
        ]
    ].head(10)
)

print("\nTotal Return Transactions:")
print(len(returns))