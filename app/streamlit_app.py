import streamlit as st
import joblib
import pandas as pd

from pathlib import Path

# -------------------------------
# Load Model + Vectorizer
# -------------------------------
MODEL_PATH = Path("model/anomaly_model.pkl")
VECT_PATH = Path("model/vectorizer.pkl")

model = joblib.load(MODEL_PATH)
vectorizer = joblib.load(VECT_PATH)

# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(
    page_title="AI Cybersecurity Log Analyzer",
    page_icon="🛡️",
    layout="wide"
)

st.title("🛡️ AI Cybersecurity Log Analyzer")
st.write("Detect anomalies in system logs using Machine Learning.")

st.markdown("---")

# -------------------------------
# File uploader
# -------------------------------
uploaded_file = st.file_uploader(
    "Upload a log file (.txt)", 
    type=["txt"],
    help="Upload system, authentication, or server logs in plain text format."
)

if uploaded_file is not None:
    logs = uploaded_file.read().decode("utf-8").splitlines()

    st.subheader("📄 Preview Logs")
    st.code("\n".join(logs[:10]))

    # Convert logs to DataFrame
    df = pd.DataFrame({"log": logs})

    # Transform text → vectors
    X = vectorizer.transform(df["log"]).toarray()

    # Predict anomalies
    predictions = model.predict(X)

    df["prediction"] = predictions
    df["label"] = df["prediction"].apply(lambda x: "ANOMALY" if x == -1 else "SAFE")

    st.markdown("---")
    st.subheader("🚨 Detection Results")

    # Highlight anomalies
    st.write(df[["log", "label"]])

    # Show counts
    st.info(
        f"**Safe logs:** {len(df[df['label']=='SAFE'])} | "
        f"**Anomalies:** {len(df[df['label']=='ANOMALY'])}"
    )

    # -------------------------------
    # Download results
    # -------------------------------
    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        label="📥 Download Results CSV",
        data=csv,
        file_name="analyzed_logs.csv",
        mime="text/csv"
    )

else:
    st.warning("Please upload a .txt log file to begin analysis.")

