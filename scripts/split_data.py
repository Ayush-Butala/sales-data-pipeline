import pandas as pd
from pathlib import Path

source_file = Path("data/source/Online Retail.xlsx")
output_folder = Path("data/raw_data")

output_folder.mkdir(parents=True, exist_ok=True)

df = pd.read_excel(source_file)

df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])

df["YearMonth"] = df["InvoiceDate"].dt.strftime("%Y_%m")

for month, data in df.groupby("YearMonth"):
    file_name = f"sales_{month}.csv"

    data.to_csv(
        output_folder / file_name,
        index=False
    )
    print(f"Created: {file_name}")