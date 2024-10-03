import pandas as pd
import sys

def analyze_csv(input_file, output_file=None):
    # Load CSV file
    try:
        df = pd.read_csv(input_file)
        print(f"File '{input_file}' loaded successfully!")
    except Exception as e:
        print(f"Error loading file: {e}")
        return

    # Show the first few rows of the DataFrame
    print("\n--- Preview of the data ---\n")
    print(df, "\n")

    # Show basic information
    print("\n--- Basic Information ---\n")
    print(df.info(), "\n")

    # Show summary statistics for numeric columns
    print("\n--- Summary Statistics ---\n")
    print(df.describe(), "\n")

    # Show unique value counts for each column
    print("\n--- Unique Value Counts for Each Column ---\n")
    for col in df.columns:
        print(f"\nUnique values in column '{col}':")
        print(df[col].value_counts())

    # Handle missing data
    missing_data = df.isnull().sum()
    print("\n--- Missing Data ---\n")
    print(missing_data)

    # Optionally, clean the data (drop rows with missing values)
    clean_option = input("\nDo you want to drop rows with missing values? (yes/no): ").lower()
    if clean_option == 'yes':
        df_cleaned = df.dropna()
        print("\n--- Data after dropping missing values ---\n")
        print(df_cleaned.info(), "\n")
    else:
        df_cleaned = df

    # Save cleaned data to a new CSV file if an output path is provided
    if output_file:
        try:
            df_cleaned.to_csv(output_file, index=False)
            print(f"\nCleaned data saved to '{output_file}'")
        except Exception as e:
            print(f"Error saving file: {e}")

if __name__ == "__main__":
    # Check for command-line arguments
    if len(sys.argv) < 2:
        print("Usage: python analyze_csv.py <input_file.csv> [output_file.csv]")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else None
        analyze_csv(input_file, output_file)
