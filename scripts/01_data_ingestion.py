# import pandas, os
# set DATA_PATH = 'data/Greenhouse Plant Growth Metrics.csv'
# load df = pd.read_csv(DATA_PATH)
# print df.shape, df.head()
# print df.isnull().sum()
# os.makedirs('outputs', exist_ok=True)
# df.to_csv('outputs/raw_data_copy.csv', index=False)
# with open('outputs/01_data_summary.txt','w') as f:
#     f.write(str(df.describe()))