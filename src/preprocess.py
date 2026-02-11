import pandas as pd

def load_logs(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        logs = f.readlines()
    logs = [line.strip() for line in logs]
    return logs

def create_dataframe(logs):
    return pd.DataFrame({"log": logs})

