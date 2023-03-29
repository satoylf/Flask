from flask import Blueprint, render_template, redirect, url_for

login = Blueprint("login", __name__, template_folder="./views/", static_folder='./static/', root_path="./")

@login.route('/')
def login_index():
    return render_template('views/auth/login.html')
