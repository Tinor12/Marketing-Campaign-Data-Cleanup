
import pandas as pd

# Step 1: Load dataset using the correct separator (TAB)
df = pd.read_csv('marketing_campaign.csv', sep='\t')

# Step 2: Clean column headers (strip spaces, lowercase, replace spaces with underscores)
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

# Step 3: Print columns to verify
print("Cleaned Columns:", df.columns.tolist())

# Step 4: Handle missing values
df['income'] = df['income'].fillna(df['income'].median())

# Step 5: Remove duplicate rows
df.drop_duplicates(inplace=True)

# Step 6: Standardize text fields
df['education'] = df['education'].str.strip().str.lower()
df['marital_status'] = df['marital_status'].str.strip().str.lower()

# Step 7: Convert date column
df['dt_customer'] = pd.to_datetime(df['dt_customer'], format='%d-%m-%Y')

# Step 8: Fix data types for selected numeric fields
df['kidhome'] = df['kidhome'].astype(int)
df['teenhome'] = df['teenhome'].astype(int)
df['income'] = df['income'].astype(float)

# Step 9: Export cleaned data to new CSV file
df.to_csv('cleaned_marketing_campaign.csv', index=False)

print("✅ Data cleaning complete. Cleaned file saved as 'cleaned_marketing_campaign.csv'")
