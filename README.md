# SEC Reporting Tie-Out

A controlled financial-statement tie-out that compares draft filing balances with general-ledger support and flags discrepancies before review.

## Tie-out visualization

![Filing-to-ledger exceptions](project-overview.svg)

## Use case

SEC reporting teams must ensure that amounts presented in financial statements and disclosures agree to approved supporting schedules. This project demonstrates a simplified, auditable tie-out process.

## Checks

- Filing amount agrees to ledger support
- Difference is within defined tolerance
- Review status is assigned consistently
- Exceptions are exported for follow-up

## Run

```bash
pip install pandas
python tie_out.py
```

The project uses synthetic data and does not reproduce confidential client information.
