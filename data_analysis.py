import pandas as pd

def analyze_data(file_path):
    df = pd.read_csv(file_path)

    print("Basic Statistics:")
    print(df.describe())

    print("\nColumn Information:")
    print(df.info())


if __name__ == "__main__":
    file = "sample_data.csv"
    analyze_data(file)
