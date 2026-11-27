from retail_anomaly import db
from retail_anomaly.pipeline import retune_threshold
if __name__ == "__main__":
    db.init_db()
    print(retune_threshold()["message"])
