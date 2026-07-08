# Local Business Lead Tracker

Open-source lightweight toolkit for small local businesses and B2B service providers that need to track leads, deals, revenue, marketing cost, and simple funnel performance without expensive CRM software.

The project is intentionally simple: CSV templates + a Python CLI report generator + practical documentation.

## Why this exists

Many local businesses get leads from messengers, classifieds, outdoor ads, referrals, websites, and direct calls, but they do not track the basic funnel:

`impressions -> views -> contacts -> deals -> revenue -> gross profit`

As a result, they often do not know:

- which channel brings real deals;
- what the cost per lead is;
- what the cost per deal is;
- which offer converts better;
- whether advertising pays back;
- where leads are lost.

This project gives a simple starting point for measuring that.

## Who it is for

- local service businesses;
- outdoor advertising and printing companies;
- repair and construction contractors;
- clinics and medical service providers;
- real estate agents;
- retail and hospitality businesses;
- small B2B teams that use messengers and spreadsheets.

## What is included

- CSV lead tracking template;
- sample dataset;
- Python report generator;
- funnel metrics documentation;
- practical website and classifieds tracking notes;
- early roadmap for a small-business lead management toolkit.

## Quick start

Requirements: Python 3.10+.

```bash
git clone https://github.com/timtimov2023/878703.git
cd 878703
python src/lead_tracker.py data/sample_leads.csv
```

Expected output:

```text
Local Business Lead Report
--------------------------
Rows: 8
Channels: avito, referrals, website, outdoor_ads, telegram

Funnel totals
Impressions: 18200
Views: 1470
Contacts: 64
Deals: 11

Conversion
View rate: 8.08%
Contact rate from views: 4.35%
Deal rate from contacts: 17.19%

Money
Ad cost: 53000.00
Revenue: 575000.00
Gross profit: 252000.00
Cost per contact: 828.12
Cost per deal: 4818.18
Marketing payback: 4.75x gross profit / ad cost
```

## CSV columns

Required columns:

| Column | Meaning |
|---|---|
| date | Date in YYYY-MM-DD format |
| channel | Lead source: avito, website, referral, telegram, outdoor_ads, etc. |
| campaign | Campaign or offer name |
| impressions | Ad or listing impressions |
| views | Listing/page/profile views |
| contacts | Messages, calls, forms, direct requests |
| deals | Closed deals |
| ad_cost | Advertising or promotion cost |
| revenue | Revenue from deals |
| gross_profit | Gross profit after direct costs |
| notes | Optional notes |

## Example use cases

### Avito / classifieds

Track each listing by week:

- impressions;
- views;
- contacts;
- deals;
- ad spend;
- revenue;
- gross profit.

### Websites

Track the path:

`offer -> trust -> lead action -> contact -> deal`

### Outdoor advertising

Track by campaign or location:

- QR scans;
- calls;
- direct mentions;
- leads;
- deals;
- payback.

## Current project status

Early-stage MVP. The project is useful as a simple template and reporting tool, but not a full CRM.

## Roadmap

See [ROADMAP.md](ROADMAP.md).

## License

MIT. See [LICENSE](LICENSE).
