import argparse
import pandas as pd
import joblib

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args()
    preprocessor = joblib.load('outputs/preprocessor.joblib')
    pca = joblib.load('outputs/pca.joblib')
    model = joblib.load('outputs/05_rf_model.joblib')
    df = pd.read_csv(args.input)
    X = df.drop(columns=['Class'], errors='ignore')
    X_proc = preprocessor.transform(X)
    X_pca = pca.transform(X_proc)
    df['Prediction'] = model.predict(X_pca)
    df.to_csv(args.output, index=False)

if __name__ == "__main__":
    main()