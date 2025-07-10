import pandas as pd

try:
    df = pd.read_csv('sample_data.csv')
    print("✅ CSV file loaded successfully!")
except FileNotFoundError:
    print("❌ CSV file not found! Please check the filename.")
    exit()

print("\n📊 Here's a preview of your data:")
print(df.head())

print("\n🧾 Available columns:")
for col in df.columns:
    print("-", col)

while True:
    user_input = input("\n🔍 Enter column name to analyze (type 'summary' for all columns, or 'exit' to quit): ").strip().lower()

    if user_input in ['exit', 'quit']:
        print("\n👋 Exiting program. Thank you, Aeshika!")
        break

    elif user_input in ['summary', 'all']:
        print("\n📊 Summary for all numeric columns:")
        numeric_cols = df.select_dtypes(include='number').columns

        for col in numeric_cols:
            print(f"\n📘 {col} ▼")
            print("🔢 Sum:", df[col].sum())
            print("📊 Average:", df[col].mean())
            print("🔺 Max:", df[col].max())
            print("🔻 Min:", df[col].min())
            print("🔢 Count:", df[col].count())

    else:
        found_col = None
        for col in df.columns:
            if col.strip().lower() == user_input:
                found_col = col
                break

        if found_col:
            print(f"\n📈 Analysis for column: {found_col}")
            if pd.api.types.is_numeric_dtype(df[found_col]):
                print("🔢 Sum:", df[found_col].sum())
                print("📊 Average:", df[found_col].mean())
                print("🔺 Max:", df[found_col].max())
                print("🔻 Min:", df[found_col].min())
                print("🔢 Count:", df[found_col].count())
            else:
                print("❌ This column is not numeric.")
        else:
            print("❌ Column not found. Please check spelling.")
