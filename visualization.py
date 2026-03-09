import pandas as pd
import matplotlib.pyplot as plt

def visualize_data(file_path):
    df = pd.read_csv(file_path)

    df.hist()
    plt.title("Data Distribution")
    plt.show()


if __name__ == "__main__":
    file = "sample_data.csv"
    visualize_data(file)
