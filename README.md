
# 🔐 AI Cybersecurity Log Analyzer  
### Machine Learning-Based Log Anomaly Detector

This project uses **Machine Learning + NLP** to detect suspicious activity inside log files.  
It’s a cybersecurity-focused AI tool that demonstrates:

✅ Log analysis  
✅ Text preprocessing  
✅ TF-IDF vectorization  
✅ Anomaly detection (Isolation Forest)  
✅ Cyber + AI integration  

---

## 🚀 Features
- Detects unusual or suspicious log events  
- Uses Isolation Forest (unsupervised anomaly detection)  
- Converts text logs into numeric vectors using TF-IDF  
- Fast, lightweight, and extendable  
- Works with any `.txt` log file  

---

## 📂 Project Structure
ai-cybersecurity-log-analyzer/
│
├── data/ # Log file samples
├── model/ # Saved trained model
├── src/ # Source code
│ ├── preprocess.py
│ ├── train_anomaly_detector.py
│ └── analyze_logs.py
└── requirements.txt


---

## 🧠 How It Works (Architecture)
1. Load log file  
2. Convert log text → vectors (TF-IDF)  
3. Train Isolation Forest  
4. Predict anomalies  
5. Output clean report of suspicious lines  

---

## ▶️ Train the Model


---

## ▶️ Analyze Logs Using Your Model



---

## 🔍 Output Example

[SAFE] User login from 192.168.1.10
[ANOMALY] Failed password attempt from unknown IP 45.9.14.122
[SAFE] File accessed: /var/log/auth.log
[ANOMALY] Multiple rapid SSH attempts detected


---

## 🛡️ Skills Demonstrated
- Cybersecurity log parsing  
- Natural Language Processing  
- TF-IDF feature extraction  
- Unsupervised anomaly detection  
- Python scripting  
- Machine learning pipeline  

---

## 📌 Future Improvements
- Add visualization dashboard (Streamlit)
- Train on larger datasets
- Add regex pre-processing for noise reduction  

---

## 👩‍💻 Author  
**Hanan Morsel**  
AI Engineer | Cybersecurity Technologist  
