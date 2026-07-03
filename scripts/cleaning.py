import pandas as pd
from pathlib import Path

# Read all monthly files
raw_data_folder = Path("data/raw_data")

files = raw_data_folder.glob("*.csv")

df_list = []

for file in files:
    df = pd.read_csv(file)
    df_list.append(df)

sales = pd.concat(df_list, ignore_index=True)

print(f"Original Rows: {len(sales):,}")

# Removing duplicate
duplicates_removed = sales.duplicated().sum()

sales = sales.drop_duplicates()

print(f"Duplicates Removed: {duplicates_removed:,}")

# Filling null values
sales["CustomerID"] = sales["CustomerID"].fillna("UNKNOWN")

sales["Description"] = sales["Description"].fillna("Unknown Product")

sales["InvoiceDate"] = pd.to_datetime(
    sales["InvoiceDate"],
    errors="coerce"
)

# Remove invalid dates if any
invalid_dates = sales["InvoiceDate"].isna().sum()

sales = sales.dropna(subset=["InvoiceDate"])

print(f"Invalid Dates Removed: {invalid_dates:,}")

# erased negative value
negative_price_rows = (sales["UnitPrice"] < 0).sum()

sales = sales[sales["UnitPrice"] >= 0]

print(f"Negative Price Rows Removed: {negative_price_rows:,}")

adjustment_rows = (
    sales["Description"]
    .astype(str)
    .str.contains(
        "Adjust bad debt",
        case=False,
        na=False
    )
).sum()

sales = sales[
    ~sales["Description"]
    .astype(str)
    .str.contains(
        "Adjust bad debt",
        case=False,
        na=False
    )
]

print(f"Accounting Adjustments Removed: {adjustment_rows:,}")

# Creating transaction type
sales["TransactionType"] = sales["Quantity"].apply(
    lambda x: "Return" if x < 0 else "Sale"
)

# Saving the new cleaned ddataset
output_file = Path(
    "data/cleaned_data/clean_sales.csv"
)
output_file.parent.mkdir(
    parents=True,
    exist_ok=True
)
sales.to_csv(
    output_file,
    index=False
)
print("\nCleaning Complete")
print(f"Final Rows: {len(sales):,}")
print(f"Saved To: {output_file}")