import pandas as pd

# Load the dataset
df = pd.read_csv(r"C:\Users\himan\OneDrive\Desktop\Coding\Elevate Labs Internship\Final Project\Shark_Tank_US_dataset.csv")

# Debug Got Deal values
print("🔍 Got Deal column values:", df["Got Deal"].unique())

# Clean currency columns
money_cols = [
    "Original Ask Amount",
    "Total Deal Amount",
    "Investment Amount Per Shark",
    "Barbara Corcoran Investment Amount",
    "Mark Cuban Investment Amount",
    "Lori Greiner Investment Amount",
    "Robert Herjavec Investment Amount",
    "Daymond John Investment Amount",
    "Kevin O Leary Investment Amount",
    "Guest Investment Amount"
]

for col in money_cols:
    if col in df.columns:
        df[col] = df[col].astype(str).str.replace(r"[$,]", "", regex=True).replace("nan", None)
        df[col] = pd.to_numeric(df[col], errors="coerce")

# ✅ Fix: match 1.0 directly for Deal
df["Deal_Status"] = df["Got Deal"].apply(lambda x: "Deal" if x == 1.0 else "No Deal")

# Drop rows where Startup or Industry is missing
df = df.dropna(subset=["Startup Name", "Industry"])

# Save cleaned CSV
df.to_csv("SharkTank_US_Cleaned.csv", index=False)

# Show Deal vs No Deal counts
print("✅ Cleaned file saved. Sample Deal_Status values:")
print(df["Deal_Status"].value_counts())
