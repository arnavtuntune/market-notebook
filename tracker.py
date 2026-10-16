"""Paper-portfolio tracker for Indian stocks.

Reads holdings.csv, pulls prices from Yahoo Finance, compares the portfolio
against the Nifty 50, and writes a monthly report to reports/YYYY-MM.md.

Usage:
    python tracker.py            # report for today
"""

import csv
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

import yfinance as yf

ROOT = Path(__file__).parent
HOLDINGS = ROOT / "holdings.csv"
REPORTS = ROOT / "reports"
BENCHMARK = "^NSEI"  # Nifty 50


def close_on(ticker: str, day: date) -> float:
    """Closing price on `day`, or the last trading day before it."""
    hist = yf.Ticker(ticker).history(start=day - timedelta(days=10), end=day + timedelta(days=1))
    if hist.empty:
        raise ValueError(f"No price data for {ticker} around {day}")
    return float(hist["Close"].iloc[-1])


def load_holdings() -> list[dict]:
    with HOLDINGS.open(newline="", encoding="utf-8") as f:
        rows = [r for r in csv.DictReader(f) if r["ticker"].strip()]
    for r in rows:
        r["qty"] = int(r["qty"])
        r["buy_date"] = datetime.strptime(r["buy_date"], "%Y-%m-%d").date()
    return rows


def main() -> None:
    sys.stdout.reconfigure(encoding="utf-8")  # Windows consoles can't print ₹ otherwise
    today = date.today()
    holdings = load_holdings()

    lines = []
    invested = current = 0.0
    for h in holdings:
        buy = close_on(h["ticker"], h["buy_date"])
        now = close_on(h["ticker"], today)
        cost, value = buy * h["qty"], now * h["qty"]
        invested += cost
        current += value
        ret = (now / buy - 1) * 100
        lines.append(
            f"| {h['ticker']} | {h['qty']} | {buy:,.2f} | {now:,.2f} | {value:,.0f} | {ret:+.1f}% | {h['thesis']} |"
        )

    # Benchmark: Nifty return since the earliest buy date
    start = min(h["buy_date"] for h in holdings)
    nifty_ret = (close_on(BENCHMARK, today) / close_on(BENCHMARK, start) - 1) * 100
    port_ret = (current / invested - 1) * 100

    report = "\n".join([
        f"# Portfolio report — {today:%B %Y}",
        "",
        f"- Invested: ₹{invested:,.0f}",
        f"- Current value: ₹{current:,.0f}",
        f"- Portfolio return: **{port_ret:+.1f}%**",
        f"- Nifty 50 since {start:%d %b %Y}: **{nifty_ret:+.1f}%**",
        f"- Beat the market? **{'Yes' if port_ret > nifty_ret else 'No'}**",
        "",
        "| Stock | Qty | Buy ₹ | Now ₹ | Value ₹ | Return | Thesis |",
        "|---|---|---|---|---|---|---|",
        *lines,
        "",
        "## What I learned this month",
        "",
        "_Write 3–5 sentences yourself: what moved, why, and was your thesis right?_",
        "",
    ])

    REPORTS.mkdir(exist_ok=True)
    out = REPORTS / f"{today:%Y-%m}.md"
    out.write_text(report, encoding="utf-8")
    print(report)
    print(f"\nSaved to {out}")


if __name__ == "__main__":
    main()
