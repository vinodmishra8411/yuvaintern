from retail_anomaly.pipeline import run_pipeline
if __name__ == "__main__":
    data, metrics, threshold = run_pipeline()
    print(f"Daily batch complete: {int(data.is_alert.sum()):,} alerts")
    print(f"Precision@Top 1% (all labelled synthetic data): {metrics['precision_at_top_1_percent']:.1%}")
