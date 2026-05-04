# cleaning.py

import pandas as pd

# -------------------------------
# STEP 1: Load Dataset
# -------------------------------
df = pd.read_csv("data/car_prices.csv")

print("✅ Dataset Loaded Successfully")
print("Shape:", df.shape)
print("\nFirst 5 rows:\n", df.head())


# -------------------------------
# STEP 2: Data Assessment
# -------------------------------
print("\n🔍 Checking Missing Values:")
print(df.isnull().sum())

print("\n🔍 Checking Duplicates:")
print("Duplicate Rows:", df.duplicated().sum())

print("\n🔍 Column Names:")
print(df.columns)


# -------------------------------
# STEP 3: Data Cleaning
# -------------------------------

# Remove duplicates
df = df.drop_duplicates()

# Fill missing values (UPDATED FIX)
df = df.ffill()

# Standardize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

print("\n✅ Cleaning Done")


# -------------------------------
# STEP 4: Data Transformation (FIXED)
# -------------------------------

# -------------------------------
# STRONG DATE FIX (FINAL)
# -------------------------------

if 'saledate' in df.columns:

    # Convert everything to string first
    df['saledate'] = df['saledate'].astype(str)

    # Clean unwanted text (if exists like timezone, etc.)
    df['saledate'] = df['saledate'].str.replace(r'UTC', '', regex=True)
    df['saledate'] = df['saledate'].str.strip()

    # Try parsing with dayfirst + utc fix
    df['saledate'] = pd.to_datetime(
        df['saledate'],
        errors='coerce',
        dayfirst=False,
        utc=True
    )

    print("\n🧪 saledate dtype after conversion:", df['saledate'].dtype)

    # Remove rows where conversion failed
    df = df[df['saledate'].notna()]

    # Convert back to normal datetime (remove timezone)
    df['saledate'] = df['saledate'].dt.tz_localize(None)

    # NOW safe to use .dt
    df['sale_year'] = df['saledate'].dt.year
    df['sale_month'] = df['saledate'].dt.month


# Create price difference column
if 'sellingprice' in df.columns and 'mmr' in df.columns:
    df['price_difference'] = df['sellingprice'] - df['mmr']

print("\n✅ Transformation Done")


# -------------------------------
# STEP 5: Final Check
# -------------------------------
print("\n📊 Final Dataset Info:")
print(df.info())

print("\n📊 Cleaned Data Preview:")
print(df.head())


# -------------------------------
# STEP 6: Save Cleaned Dataset
# -------------------------------
df.to_csv("data/cleaned_sales.csv", index=False)

print("\n💾 Cleaned dataset saved as 'cleaned_sales.csv'")