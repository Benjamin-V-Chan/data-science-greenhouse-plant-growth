import os
import pandas as pd
import matplotlib.pyplot as plt

def main():
    os.makedirs('outputs', exist_ok=True)
    df = pd.read_csv('data/Greenhouse Plant Growth Metrics.csv')
    df.describe().to_csv('outputs/03_descriptive_stats.csv')
    numerical_cols = [c for c in df.columns if df[c].dtype in ['float64','int64']]
    for col in numerical_cols:
        plt.hist(df[col], bins=30)
        plt.title(col)
        plt.savefig(f'outputs/03_hist_{col}.png')
        plt.clf()
    corr = df[numerical_cols].corr()
    plt.imshow(corr, cmap='coolwarm', interpolation='none')
    plt.colorbar()
    plt.title('Correlation Heatmap')
    plt.savefig('outputs/03_corr_heatmap.png')
    plt.clf()
    df['Class'].value_counts().plot.bar()
    plt.title('Class Distribution')
    plt.savefig('outputs/03_class_dist.png')
    plt.clf()

if __name__ == "__main__":
    main()