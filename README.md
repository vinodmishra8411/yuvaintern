# Retail Anomaly Command Centre (Advanced Edition)

AI fraud and anomaly monitoring for a (fictional) Delhi supermarket chain: 5 ML algorithms, a 0-100 risk score, live transaction
monitoring, explainable alerts (English + Hinglish), case management, reports, email alerts, login with roles, and a themed dashboard.

## Quick start
**Windows:** double-click `START_DASHBOARD.bat`.  **Mac/Linux:** `./START_DASHBOARD.sh`.
Or manually (Python 3.10+):
```bash
python -m venv .venv
.venv\Scripts\activate          # Mac/Linux: source .venv/bin/activate
pip install -r requirements.txt
streamlit run dashboard.py
```
First launch creates 50,000 sample transactions and trains the models (about 1 minute). No other setup is needed.

**Demo logins** (change them in Admin Panel -> Users):

| Role | Username | Password | Can do |
|---|---|---|---|
| Admin | `admin` | `Admin@123` | everything, incl. Admin Panel |
| Analyst | `analyst` | `Analyst@123` | review/edit alerts, reports, retrain |
| Viewer | `viewer` | `Viewer@123` | read-only dashboards and reports |

## Where each requested feature lives
| # | Feature | Where |
|---|---|---|
| 1 | Multiple ML algorithms | Isolation Forest, Local Outlier Factor, One-Class SVM, Autoencoder, Robust Z-Score, combined as an ensemble (`models.py`; compare in **Model Lab**) |
| 2 | Real-time monitoring | **Live Monitor** (simulated POS stream scored transaction by transaction) |
| 3 | AI-based fraud detection | Ensemble of the 5 unsupervised models (no fraud labels needed to run) |
| 4 | Dynamic risk score 0-100 | `risk_score` + bands Low / Medium / High / Critical, recalculated for every transaction; threshold re-tuned weekly from reviewer feedback |
| 5 | Explainable AI | Reason codes and plain-language text in English/Hinglish, contribution chart, per-model votes (**Explorer & Explain**, **Alert Management**) |
| 6 | Customer behaviour | **Customers**: segments, guest vs known, shopping-time heatmap, per-customer profile |
| 7 | Store-wise risk | **Stores & Map**: risk index, gauges, ranking, daily trend |
| 8 | Fraud heatmaps | **Stores & Map -> Fraud heatmaps** (store x hour, category x store, weekday x hour, payment x category) |
| 9 | AI chatbot | **AI Assistant** (answers from your data; optional Claude for open questions) |
| 10 | Automatic email alerts | Critical alerts are emailed automatically (SMTP) or saved to `outputs/email_outbox/` |
| 11 | Alert management | Status workflow, priority, assignee, notes, bulk actions, case history, SLA/overdue |
| 12 | PDF / Excel / CSV reports | **Reports** |
| 13 | Model accuracy monitoring | **Model Lab**: precision/recall, ROC/PR, confusion matrix, daily accuracy, drift (PSI), reviewer-confirmed precision |
| 14 | Login and admin panel | Roles, user management, thresholds, SMTP, audit log, email log, system tools |
| 15 | Dark / light mode | Sidebar toggle |
| 16-17 | Animated KPI cards, live charts | Count-up KPI cards with sparklines; Plotly charts; auto-refreshing live view |
| 18 | Interactive map | Delhi store map with alert dots (needs internet for map tiles) |
| 19 | Real-time activity feed | Command Center and Live Monitor |
| 20-22 | Sidebar navigation, search and filters, fullscreen | Sidebar: quick search, date/store/risk filters, Fullscreen button |

## Command line
```bash
python generate_data.py --rows 300000   # optional larger dataset (300k rows: ~20 s training, ~1.2 GB RAM)
python train.py                         # fit baselines + models, score everything, sync alert cases
python batch_score.py                   # daily batch job (same pipeline, prints headline accuracy)
python weekly_tune.py                   # re-tune the alert threshold from reviewer decisions
python tests/smoke_test.py              # runs every dashboard page against your data with stubbed UI
```

## Email alerts
Admin Panel -> Settings & Email. For Gmail use host `smtp.gmail.com`, port 587, STARTTLS, and an **app password**.
You can keep the password out of the settings file by setting the `SMTP_PASSWORD` environment variable.
Without SMTP details, every alert email is written to `outputs/email_outbox/` and listed in the email log.

## AI Assistant with Claude (optional)
The assistant works offline. For open-ended questions install `anthropic` (`pip install anthropic`) and set `ANTHROPIC_API_KEY`; it then sends only a short data summary to Claude.

## Using your own data
Replace `data/transactions.csv` (columns: transaction_id, timestamp, customer_id, store_id, category_raw, quantity, unit_price_raw, gst_rate,
gst_inclusive_flag, amount, payment_method; optional `label` for accuracy metrics) and run `python train.py`. Store map coordinates are in `retail_anomaly/config.py`.

## Files
`dashboard.py` entry point · `retail_anomaly/` (generator, features, models, explain, pipeline, db, notify, reports, chatbot, theme, ui) ·
`outputs/` (scored data, model, database, settings, email outbox; created automatically) · `notebooks/` · `tests/`

## Honest limitations
- All data is **synthetic**; labels come from the same generator, so accuracy figures are optimistic compared with real fraud.
- Weakest detections on the demo data: spend spikes (34% caught), velocity bursts (36%), guest high-value (39%). Night-time cash and quantity spikes are caught at 100%.
- The login system is for demonstration and a trusted network. Do not expose it to the internet without HTTPS and a hardened identity provider; change the demo passwords.
- Dark/light switching is done with CSS on top of Streamlit, so a few native widgets may look slightly different between modes.
- The map needs internet access for tiles. Email via SMTP depends on your mail provider's settings.
- The dashboard UI was verified with an automated smoke test that exercises all page logic, not by clicking through a browser. If something looks off in your browser or Streamlit version, check `streamlit --version` (>= 1.37 required).
