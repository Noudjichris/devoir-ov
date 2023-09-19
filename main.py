from pathlib import Path
# MBAIGOLNOUDJI CHRISTIAN MASTER II Data Analyst
list_repertoires = ["data/cleaned","data/processed","data/raw", "docs", "models", "notebooks", "reports", "src"]
list(map(lambda x: Path(x).mkdir(parents=True, exist_ok=True), list_repertoires))
