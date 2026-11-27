import argparse
from retail_anomaly.generator import generate_transactions
from retail_anomaly.config import TRANSACTIONS
if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Generate synthetic retail transactions")
    p.add_argument("--rows", type=int, default=100000)
    p.add_argument("--seed", type=int, default=42)
    a = p.parse_args()
    TRANSACTIONS.parent.mkdir(exist_ok=True)
    generate_transactions(a.rows, a.seed).to_csv(TRANSACTIONS, index=False)
    print(f"Generated {a.rows:,} rows -> {TRANSACTIONS}")
