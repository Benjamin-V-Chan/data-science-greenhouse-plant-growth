import os
import joblib
import numpy as np
from sklearn.decomposition import PCA

def main():
    os.makedirs('outputs', exist_ok=True)
    X_train, X_test, y_train, y_test = joblib.load('outputs/train_test_split.joblib')

    # Ratio Features    
    ratio_train = X_train[:,2] / (X_train[:,4] + 1e-6)
    ratio_test = X_test[:,2] / (X_test[:,4] + 1e-6)
    X_train_fe = np.hstack([X_train, ratio_train.reshape(-1,1)])
    X_test_fe = np.hstack([X_test, ratio_test.reshape(-1,1)])
    pca = PCA(n_components=0.95, random_state=42)
    X_train_pca = pca.fit_transform(X_train_fe)
    X_test_pca = pca.transform(X_test_fe)
    joblib.dump(pca, 'outputs/pca.joblib')
    joblib.dump((X_train_pca, X_test_pca, y_train, y_test), 'outputs/engineered_data.joblib')

if __name__ == "__main__":
    main()