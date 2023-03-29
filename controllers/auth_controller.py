from flask import Blueprint, render_template, redirect, url_for

auth = Blueprint("auth", __name__, template_folder="./views/", static_folder='./static/', root_path="./")

@auth.route("/")
def auth_index():
    return redirect(url_for('auth.login_index'))

@auth.route('/login')
def login_index():
    return render_template('auth/login.html')

@auth.route("/cadastro")
def cadastro_index():
    return render_template("auth/cadastro.html")