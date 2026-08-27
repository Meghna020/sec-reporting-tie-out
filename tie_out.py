from pathlib import Path
import pandas as pd

ROOT = Path(__file__).resolve().parent
TOLERANCE = 1.0


def main() -> None:
    filing = pd.read_csv(ROOT / "draft_filing.csv")
    support = pd.read_csv(ROOT / "ledger_support.csv")
    tie_out = filing.merge(support, on="line_item", how="outer")
    tie_out["difference"] = tie_out["filing_amount"].fillna(0) - tie_out["ledger_amount"].fillna(0)
    tie_out["status"] = tie_out["difference"].abs().le(TOLERANCE).map({True: "Tied", False: "Review"})

    output_dir = ROOT / "outputs"
    output_dir.mkdir(exist_ok=True)
    tie_out.to_csv(output_dir / "tie_out_results.csv", index=False)
    tie_out.loc[tie_out["status"] == "Review"].to_csv(output_dir / "exceptions.csv", index=False)
    print(tie_out.to_string(index=False))


if __name__ == "__main__":
    main()
