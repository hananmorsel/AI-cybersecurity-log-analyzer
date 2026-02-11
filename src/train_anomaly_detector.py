import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import IsolationForest
from preprocess import load_logs, create_dataframe

logs = load_logs("data/sample_logs.txt")
df = create_dataframe(logs)

vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(df["log"])

model = IsolationForest(contamination=0.2, random_state=42)
model.fit(X.toarray())

joblib.dump(model, "model/anomaly_model.pkl")
joblib.dump(vectorizer, "model/vectorizer.pkl")

print("✅ Model trained and saved!")

