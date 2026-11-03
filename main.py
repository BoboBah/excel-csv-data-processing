import pandas as pd

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("input")
parser.add_argument("output")

args = parser.parse_args()

print("Input:", args.input)
print("Output:", args.output)

if args.input.endswith(".csv"):
    df = pd.read_csv(args.input)

elif args.input.endswith(".xlsx"):
    df = pd.read_excel(args.input)

else:
    raise ValueError("Unsupported file format")

try:

    df = pd.read_csv(args.input)

except FileNotFoundError:

    print("ERROR: Input file was not found.")

except Exception as e:

    print(f"ERROR: {e}")

df = pd.read_csv(input_file)

required_columns = ["name", "email", "age", "country"]

for column in required_columns:
    if column not in df.columns:
        raise ValueError(f"Missing required column: {column}")
    
df["name"] = df["name"].str.strip()
df["email"] = df["email"].str.strip()
df["country"] = df["country"].str.strip()

df["email"] = df["email"].str.lower()

duplicate_count = df.duplicated().sum()

print("Duplicates:", duplicate_count)

df = df.drop_duplicates()

missing_values = df.isnull().sum()

print(missing_values)

invalid_email = df["email"].isnull().sum()

print("Missing emails:", invalid_email)

df = df.dropna(subset=["email"])

df["age"] = pd.to_numeric(df["age"], errors="coerce")

email_pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

valid_email = df["email"].str.match(
    email_pattern,
    na=False
)
invalid_email_count = (~valid_email).sum()

print("Invalid emails:", invalid_email_count)

df = df[df["country"] == "Senegal"]
df = df[
    (df["age"] >= 18) &
    (df["age"] <= 60)
]

df = df.sort_values("name")
output_file = "output.csv"

df.to_csv(output_file, index=False)

print(f"Output created: {output_file}")

print(df)

total_records = len(df)

summary = {
    "Total records": total_records,
    "Valid records": valid_records,
    "Invalid records": invalid_records,
    "Duplicate records": duplicate_count
}

print("\nProcessing Summary")
print("------------------")

for key, value in summary.items():
    print(f"{key}: {value}")