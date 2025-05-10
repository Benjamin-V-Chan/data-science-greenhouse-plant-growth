import os
import joblib
import numpy as np
import matplotlib.pyplot as plt

def main():
    os.makedirs('outputs', exist_ok=True)
    X_train_pca, X_test_pca, y_train, y_test = joblib.load('outputs/engineered_data.joblib')
    model = joblib.load('outputs/05_rf_model.joblib')
    importances = model.feature_importances_
    idxs = np.argsort(importances)[::-1][:10]
    plt.bar(range(10), importances[idxs])
    plt.xticks(range(10), idxs)
    plt.ylabel('Importance')
    plt.title('Top 10 Feature Importances')
    plt.savefig('outputs/07_feature_importance.png')
    plt.clf()
    # PCA scatter on first two components
    plt.scatter(X_test_pca[:,0], X_test_pca[:,1], c=y_test.map({c:i for i,c in enumerate(sorted(set(y_test)))}))
    plt.xlabel('PC1')
    plt.ylabel('PC2')
    plt.title('PCA Scatter by Class')
    plt.savefig('outputs/07_pca_scatter.png')
    plt.clf()

if __name__ == "__main__":
    main()