import csv
import os

CSV_FILE = "posts.csv"

# Garante que o arquivo existe
def ensure_csv_exists():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["title", "content"])  # cabeçalho

# Ler posts do CSV
def read_posts():
    ensure_csv_exists()
    posts = []
    with open(CSV_FILE, "r", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            posts.append({"title": row["title"], "content": row["content"]})
    return posts

# Salvar todos os posts no CSV (sobrescreve)
def save_posts(posts):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "content"])
        writer.writeheader()
        writer.writerows(posts)

# Acrescentar um único post
def append_post(post):
    ensure_csv_exists()
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["title", "content"])
        writer.writerow(post)