from retail_anomaly.pipeline import run_pipeline
if __name__ == "__main__":
    data, metrics, threshold = run_pipeline()
    print(f"Scored {len(data):,} transactions; alert risk threshold={threshold:.1f}")
    print({k: v for k, v in metrics.items() if k in ("precision_at_top_1_percent", "auc", "avg_precision", "alert_recall", "max_psi", "weights")})
