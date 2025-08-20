from flask import Flask
from .funcoes import read_posts, ensure_csv_exists
from . import admin, main

def create_app():
    app = Flask(__name__)

    # Garante a existência do CSV
    ensure_csv_exists()
    app.posts = read_posts()

    # Registra rotas
    app.register_blueprint(main.main)
    app.register_blueprint(admin.admin)

    return app