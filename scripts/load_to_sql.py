import sqlite3
import pandas as pd
from pathlib import Path

csv_file = Path("data/cleaned_data/analytics_sales.csv")
db_folder = Path("database")
db_folder.mkdir(parents=True, exist_ok=True)

db_file = db_folder / "sales_pipeline.db"

sales = pd.read_csv(csv_file)

print(f"Rows Loaded from CSV: {len(sales):,}")

conn = sqlite3.connect(db_file)

sales.to_sql(
    "sales",
    conn,
    if_exists="replace",
    index=False
)

cursor = conn.cursor()

cursor.execute("SELECT COUNT(*) FROM sales")

row_count = cursor.fetchone()[0]

print("\nDatabase Load Complete!")
print(f"Rows in Database: {row_count:,}")

conn.close()

print(f"Database Saved To: {db_file}")