# Market Notebook

My paper portfolio of Indian stocks, a monthly performance report against the Nifty 50, and my own research notes. I started this in Class 11 to learn investing by actually doing it. No real money is involved.

## What's here

| Folder / file | What it is |
|---|---|
| `holdings.csv` | My paper portfolio: stock, quantity, buy date, and **why I bought it** |
| `tracker.py` | Pulls live prices, calculates my returns, compares them with the Nifty 50 |
| `reports/` | One report per month, with what I learned |
| `notes/` | My one-page stock and sector notes |

## Run it

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python tracker.py
```

## Rules I follow

1. Every stock needs a written reason before I "buy" it.
2. I don't delete bad picks. Being wrong and explaining why is part of learning.
3. One report and one note every month.
