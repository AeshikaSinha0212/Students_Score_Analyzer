# 📊 CSV Analyzer

A terminal-based CSV analyzer built by **Aeshika** using Python and Pandas.

## 📁 Features
- Loads CSV with safety check
- Displays all columns
- Analyze any numeric column:
  - Sum, Average, Max, Min, Count
- Option to view all columns summary
- Runs interactively in loop
# 📊 Student Marks Analyzer

---

## 🛠️ Technologies Used

| Tool     | Purpose                      |
|----------|------------------------------|
| Python   | Main programming language    |
| Pandas   | Data loading and statistics  |

---

## 🗂️ CSV Format Example (`sample_data.csv`)

```csv
Name,Accountancy,Economics,IT,B.st
Rachel,85,96,98,90
Amanda,75,82,97,88
Samantha,91,85,77,68
Robin,89,72,94,65
Henry,99,84,78,87
```

## ▶️ Run Instructions
1. Put `sample_data.csv` in same folder
2. Run `csv_analyzer.py` in terminal
3. Follow prompts!

import pandas as pd

try:
    df = pd.read_csv('/storage/emulated/0/pydroidfile/sample_data.csv')
    print("✅ CSV file loaded successfully!")
except FileNotFoundError:
    print("❌ CSV file not found! Please check the filename.")
    exit()

# Preview
print("\n📊 Here's a preview of your data:")
print(df.head())

# Show columns
print("\n🧾 Available columns:")
for col in df.columns:
    print("-", col)

# Start input loop
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
        # Smart match for individual column
        found_col = None
        for col in df.columns:
            if col.strip().lower() == user_input:
                found_col = col
                break

        if found_col:
            print(f"\n📈 Analysis for column: {found_col}")
            if pd.api.types9.is_numeric_dtype(df[found_col]):
                print("🔢 Sum:", df[found_col].sum())
                print("📊 Average:", df[found_col].mean())
                print("🔺 Max:", df[found_col].max())
                print("🔻 Min:", df[found_col].min())
                print("🔢 Count:", df[found_col].count())
            else:
                print("❌ This column is not numeric.")
        else:
            print("❌ Column not found. Please check spelling.")

---

👩‍💻 Built with 💙 by Aeshika
