# import pandas, joblib, argparse, os
# parser = argparse.ArgumentParser(); parser.add_argument('--input', ...); parser.add_argument('--output', ...)
# args = parser.parse_args()
# load preprocessor, pca, model from 'outputs'
# df_new = pd.read_csv(args.input)
# X_new = preprocessor.transform(df_new.drop(columns=['Class'], errors='ignore'))
# X_new_pca = pca.transform(X_new)
# preds = model.predict(X_new_pca)
# df_new['Prediction'] = preds
# df_new.to_csv(args.output, index=False)
