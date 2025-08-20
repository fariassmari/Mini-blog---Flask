from flask import Blueprint, render_template, request, redirect, url_for, current_app
from app.funcoes import save_posts, append_post
from . import admin

@admin.route("/admin")
def admin_page():
    return render_template("admin.html")

@admin.route("/create", methods=["POST"])
def create_post():
    title = request.form["title"]
    content = request.form["content"]
    post = {"title": title, "content": content}

    current_app.posts.append(post)
    append_post(post)

    return redirect(url_for("main.index"))