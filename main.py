from pathlib import Path
# MBAIGOLNOUDJI CHRISTIAN MASTER II Data Analyst
list_repertoires = ["data/cleaned","data/processed","data/raw", "docs", "models", "notebooks", "reports", "src"]
list(map(lambda x: Path(x).mkdir(parents=True, exist_ok=True), list_repertoires))


#creer une liste de fichiers
list_fichiers = ["LICENSE", "Makefile", "README.md","notebooks/main.ipynb", ".gitignore", "requirements.txt","src/utils.py","src/process.py","src/train.py"]

#creer les fichierd
list(map(lambda x: Path(x).touch(exist_ok=True), list_fichiers))