# Contributing

This project is early-stage and focused on practical tools for small local businesses.

Good contributions:

- better templates;
- clearer documentation;
- examples for real local business workflows;
- bug fixes;
- simple features that do not make the project heavy;
- translations.

Please avoid:

- complex enterprise CRM logic;
- scraping or bypassing platform rules;
- adding paid external dependencies without a strong reason.

## Development

Run the sample report:

```bash
python src/lead_tracker.py data/sample_leads.csv
```

Run tests:

```bash
python -m unittest discover tests
```
