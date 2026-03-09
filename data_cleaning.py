import pandas as pd

def clean_data(file_path):
    df = pd.read_csv(file_path)

    print("Original Data:")
    print(df.head())

    # Remove duplicate rows
    df = df.drop_duplicates()

    # Fill missing values
    df = df.fillna(method='ffill')

    print("\nCleaned Data:")
    print(df.head())

    return df


if __name__ == "__main__":
    file = "sample_data.csv"
    clean_data(file)
