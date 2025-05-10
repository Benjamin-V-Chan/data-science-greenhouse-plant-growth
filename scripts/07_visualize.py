# import joblib, matplotlib.pyplot, numpy, os
# load best model (e.g., RandomForest), pca, X_test_pca, y_test, feature names
# if RandomForest: importances = model.feature_importances_; sorted_indices = np.argsort(importances)[::-1]
# plot bar of top 10 importances; save 'outputs/07_feature_importance.png'
# plot PCA scatter: plt.scatter(X_test_pca[:,0], X_test_pca[:,1], c=label_encoding(y_test)); save 'outputs/07_pca_scatter.png'
