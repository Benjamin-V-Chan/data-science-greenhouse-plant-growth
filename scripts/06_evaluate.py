import os
import joblib
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix

def plot_cm(cm, path):
    plt.imshow(cm, cmap='Blues', interpolation='nearest')
    plt.colorbar()
    plt.xlabel('Predicted')
    plt.ylabel('Actual')
    plt.savefig(path)
    plt.clf()

def main():
    os.makedirs('outputs', exist_ok=True)
    X_train_pca, X_test_pca, y_train, y_test = joblib.load('outputs/engineered_data.joblib')
    for name in ['rf', 'lr']:
        model = joblib.load(f'outputs/05_{name}_model.joblib')
        y_pred = model.predict(X_test_pca)
        report = classification_report(y_test, y_pred, output_dict=True)
        pd.DataFrame(report).T.to_csv(f'outputs/06_{name}_report.csv')
        cm = confusion_matrix(y_test, y_pred)
        plot_cm(cm, f'outputs/06_{name}_confusion.png')

if __name__ == "__main__":
    main()