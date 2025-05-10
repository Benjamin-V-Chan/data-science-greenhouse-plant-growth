# import pandas, numpy, sklearn.decomposition PCA, joblib, os
# load preprocessor, train_test_split from 'outputs'
# X_train, X_test, y_train, y_test = loaded
# optionally generate new features on X_train, X_test (e.g., ratios)
# fit pca = PCA(n_components=0.95) on X_train; X_train_pca = pca.transform(X_train); X_test_pca = pca.transform(X_test)
# os.makedirs('outputs', exist_ok=True)
# joblib.dump(pca, 'outputs/pca.joblib')
# joblib.dump((X_train_pca, X_test_pca, y_train, y_test), 'outputs/engineered_data.joblib')
