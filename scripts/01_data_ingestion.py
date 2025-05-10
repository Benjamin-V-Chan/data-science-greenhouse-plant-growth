import os
import pandas as pd

def main():
    os.makedirs('outputs', exist_ok=True)
    df = pd.read_csv('data/Greenhouse Plant Growth Metrics.csv')
    print(f"Loaded data with shape: {df.shape}")
    print(df.head())
    print("Missing values per column:")
    print(df.isnull().sum())
    df.to_csv('outputs/raw_data_copy.csv', index=False)
    with open('outputs/01_data_summary.txt', 'w') as f:
        f.write(df.describe().to_string())

if __name__ == "__main__":
    main()