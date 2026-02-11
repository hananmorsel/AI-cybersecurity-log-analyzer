
import joblib
from preprocess import load_logs, create_dataframe

vectorizer = joblib.load("model/vectorizer.pkl")
model = joblib.load("model/anomaly_model.pkl")

logs = load_logs("data/sample_logs.txt")
df = create_dataframe(logs)

X = vectorizer.transform(df["log"]).toarray()
preds = model.predict(X)

for log, pred in zip(logs, preds):
    label = "[ANOMALY]" if pred == -1 else "[SAFE]"
    print(f"{label}  {log}")
