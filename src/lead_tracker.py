#!/usr/bin/env python3
"""
Local Business Lead Tracker

Reads a CSV file and prints simple funnel, cost, and payback metrics.

Usage:
    python src/lead_tracker.py data/sample_leads.csv
"""

from __future__ import annotations

import csv
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable


@dataclass
class LeadRow:
    date: str
    channel: str
    campaign: str
    impressions: int
    views: int
    contacts: int
    deals: int
    ad_cost: float
    revenue: float
    gross_profit: float
    notes: str = ""


def parse_int(value: str) -> int:
    value = (value or "").strip()
    if value == "":
        return 0
    return int(float(value))


def parse_float(value: str) -> float:
    value = (value or "").strip()
    if value == "":
        return 0.0
    return float(value)


def read_rows(csv_path: Path) -> list[LeadRow]:
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV file not found: {csv_path}")

    rows: list[LeadRow] = []

    with csv_path.open("r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        required = {
            "date",
            "channel",
            "campaign",
            "impressions",
            "views",
            "contacts",
            "deals",
            "ad_cost",
            "revenue",
            "gross_profit",
            "notes",
        }

        missing = required - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"Missing required columns: {', '.join(sorted(missing))}")

        for raw in reader:
            rows.append(
                LeadRow(
                    date=(raw.get("date") or "").strip(),
                    channel=(raw.get("channel") or "unknown").strip(),
                    campaign=(raw.get("campaign") or "").strip(),
                    impressions=parse_int(raw.get("impressions", "")),
                    views=parse_int(raw.get("views", "")),
                    contacts=parse_int(raw.get("contacts", "")),
                    deals=parse_int(raw.get("deals", "")),
                    ad_cost=parse_float(raw.get("ad_cost", "")),
                    revenue=parse_float(raw.get("revenue", "")),
                    gross_profit=parse_float(raw.get("gross_profit", "")),
                    notes=(raw.get("notes") or "").strip(),
                )
            )

    return rows


def safe_divide(numerator: float, denominator: float) -> float:
    if denominator == 0:
        return 0.0
    return numerator / denominator


def percentage(value: float) -> str:
    return f"{value * 100:.2f}%"


def money(value: float) -> str:
    return f"{value:.2f}"


def unique_channels(rows: Iterable[LeadRow]) -> list[str]:
    return sorted({row.channel for row in rows if row.channel})


def totals(rows: list[LeadRow]) -> dict[str, float]:
    return {
        "impressions": sum(row.impressions for row in rows),
        "views": sum(row.views for row in rows),
        "contacts": sum(row.contacts for row in rows),
        "deals": sum(row.deals for row in rows),
        "ad_cost": sum(row.ad_cost for row in rows),
        "revenue": sum(row.revenue for row in rows),
        "gross_profit": sum(row.gross_profit for row in rows),
    }


def print_report(rows: list[LeadRow]) -> None:
    data = totals(rows)

    impressions = data["impressions"]
    views = data["views"]
    contacts = data["contacts"]
    deals = data["deals"]
    ad_cost = data["ad_cost"]
    gross_profit = data["gross_profit"]

    view_rate = safe_divide(views, impressions)
    contact_rate = safe_divide(contacts, views)
    deal_rate = safe_divide(deals, contacts)
    cost_per_contact = safe_divide(ad_cost, contacts)
    cost_per_deal = safe_divide(ad_cost, deals)
    payback = safe_divide(gross_profit, ad_cost)

    print("Local Business Lead Report")
    print("--------------------------")
    print(f"Rows: {len(rows)}")
    print(f"Channels: {', '.join(unique_channels(rows)) or 'none'}")
    print()
    print("Funnel totals")
    print(f"Impressions: {int(impressions)}")
    print(f"Views: {int(views)}")
    print(f"Contacts: {int(contacts)}")
    print(f"Deals: {int(deals)}")
    print()
    print("Conversion")
    print(f"View rate: {percentage(view_rate)}")
    print(f"Contact rate from views: {percentage(contact_rate)}")
    print(f"Deal rate from contacts: {percentage(deal_rate)}")
    print()
    print("Money")
    print(f"Ad cost: {money(ad_cost)}")
    print(f"Revenue: {money(data['revenue'])}")
    print(f"Gross profit: {money(gross_profit)}")
    print(f"Cost per contact: {money(cost_per_contact)}")
    print(f"Cost per deal: {money(cost_per_deal)}")
    print(f"Marketing payback: {payback:.2f}x gross profit / ad cost")


def main(argv: list[str]) -> int:
    if len(argv) != 2:
        print("Usage: python src/lead_tracker.py data/sample_leads.csv", file=sys.stderr)
        return 2

    csv_path = Path(argv[1])

    try:
        rows = read_rows(csv_path)
        print_report(rows)
    except Exception as error:
        print(f"Error: {error}", file=sys.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
