# import pandas, matplotlib.pyplot, os
# load df = pd.read_csv('data/Greenhouse Plant Growth Metrics.csv')
# os.makedirs('outputs', exist_ok=True)
# df.describe().to_csv('outputs/03_descriptive_stats.csv')
# for col in numerical_cols:
#     plt.hist(df[col]); plt.title(col); plt.savefig(f'outputs/03_hist_{col}.png'); plt.clf()
# corr = df[numerical_cols].corr()
# plt.imshow(corr, cmap='coolwarm'); plt.colorbar(); plt.savefig('outputs/03_corr_heatmap.png'); plt.clf()
# df['Class'].value_counts().plot.bar(); plt.savefig('outputs/03_class_dist.png'); plt.clf()
