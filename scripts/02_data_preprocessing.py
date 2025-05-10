# import pandas, sklearn Pipeline components, joblib, os
# load df = pd.read_csv('data/Greenhouse Plant Growth Metrics.csv')
# define X = df.drop('Class', axis=1), y = df['Class']
# identify categorical_cols = ['Random'], numerical_cols = all others except y
# build numeric_transformer = Pipeline([('scaler', StandardScaler())])
# build categorical_transformer = Pipeline([('encoder', OneHotEncoder(sparse=False, handle_unknown='ignore'))])
# build preprocessor = ColumnTransformer(transformers=[('num', numeric_transformer, numerical_cols),
#                                                     ('cat', categorical_transformer, categorical_cols)])
# X_processed = preprocessor.fit_transform(X)
# split X_train, X_test, y_train, y_test = train_test_split(..., stratify=y)
# os.makedirs('outputs', exist_ok=True)
# joblib.dump(preprocessor, 'outputs/preprocessor.joblib')
# joblib.dump((X_train, X_test, y_train, y_test), 'outputs/train_test_split.joblib')
