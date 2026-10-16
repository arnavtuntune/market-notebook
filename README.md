# market-notebook

Paper portfolio of NSE stocks (₹2 lakh, no real money), started 16 Oct 2026.

Every position has a written thesis in `holdings.csv`. Once a month `tracker.py` pulls prices, compares returns with the Nifty 50 and writes a report to `reports/`, and I add what I got right or wrong. Longer notes on individual companies go in `notes/`.

Bad picks stay in. The point is to see how my reasoning holds up.

## Current holdings

| Stock | Sector |
|---|---|
| HDFC Bank | Banking |
| Bharti Airtel | Telecom |
| Larsen & Toubro | Infrastructure |
| Titan | Consumer / jewellery |
| Sun Pharma | Pharma |
| TCS | IT services |
| Maruti Suzuki | Autos |

## Running it

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python tracker.py
```

`publish.ps1` commits and pushes the month's report and notes.
