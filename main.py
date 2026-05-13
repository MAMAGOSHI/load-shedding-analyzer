import pandas as pd
import matplotlib.pyplot as plt
import os

def load_data(file_path):
    return pd.read_csv(file_path)


def create_charts(df):

    # Ensure charts folder exists
    if not os.path.exists("charts"):
        os.makedirs("charts")

    numeric_cols = df.select_dtypes(include=['number']).columns

    if len(numeric_cols) == 0:
        print("No numeric columns found.")
        return

    # Use up to 3 numeric columns
    for i, col in enumerate(numeric_cols[:3]):
        plt.figure(figsize=(10, 5))
        plt.plot(df[col])
        plt.title(f"{col} Trend")
        plt.xlabel("Index")
        plt.ylabel(col)
        plt.grid(True)

        filename = f"charts/chart_{i+1}.png"
        plt.savefig(filename)
        plt.close()

        print(f"Saved: {filename}")


def main():
    file_path = "data/raw/EskomSePush_history.csv"

    try:
        print("Loading dataset...")
        data = load_data(file_path)

        print("Dataset loaded successfully.")

        create_charts(data)

        print("All charts created successfully.")

    except FileNotFoundError:
        print("File not found. Check dataset path.")

    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()