import pandas as pd

df = pd.read_csv("./raw_withoutbucket_10000.csv")

# Display original shape
print(f"Original data shape: {df.shape}")

# Select the last column
last_col = df.columns[25]

# Convert last column to numeric, coerce errors into NaN
df[last_col] = pd.to_numeric(df[last_col], errors='coerce')

# Drop rows where last column became NaN
df_cleaned = df.dropna(subset=[last_col])

# Display new shape after cleaning
print(f"Cleaned data shape: {df_cleaned.shape}")

# Save to a new CSV file
df_cleaned.to_csv("./corrected_data_10k.csv", index=False)

print("Cleaned file saved")
