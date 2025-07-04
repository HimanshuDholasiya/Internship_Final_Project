import pandas as pd

# Load the cleaned Shark Tank US dataset
df = pd.read_csv(r"C:\Users\himan\OneDrive\Desktop\Coding\Elevate Labs Internship\Final Project\SharkTank_US_Cleaned.csv")


# Calculate total investment by each shark
sharks = {
    "Mark Cuban": df["Mark Cuban Investment Amount"].sum(),
    "Lori Greiner": df["Lori Greiner Investment Amount"].sum(),
    "Kevin O Leary": df["Kevin O Leary Investment Amount"].sum(),
    "Daymond John": df["Daymond John Investment Amount"].sum(),
    "Robert Herjavec": df["Robert Herjavec Investment Amount"].sum(),
    "Barbara Corcoran": df["Barbara Corcoran Investment Amount"].sum(),
    "Guest Investor": df["Guest Investment Amount"].sum()
}

# Convert the dictionary to a DataFrame
shark_df = pd.DataFrame(list(sharks.items()), columns=["Shark", "Total Investment"])

# Save to a new CSV file
shark_df.to_csv("Shark_Investments_Summary.csv", index=False)

print("✅ Shark investment summary saved as 'Shark_Investments_Summary.csv'")
