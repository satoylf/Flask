from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_user, login_required, logout_user, current_user
from models import User, db
from werkzeug.security import generate_password_hash, check_password_hash
from models.auth.user import User   

auth = Blueprint("auth", __name__, template_folder="./views/", static_folder='./static/', root_path="./")

@auth.route("/")
@auth.route("/login")
def login():
    return render_template("auth/login.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@auth.route('/admin')
@login_required
def auth_admin():
     return render_template("admin_base.html", name=current_user.name)
@auth.route('/login_post', methods=['POST'])
def login_post():
    # login code goes here
    login_info = request.form.get('login')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    
    user = User.query.filter_by(email=login_info).first()

    if not user or not check_password_hash(user.password, password):
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login'))
    login_user(user, remember=remember)

    return redirect(url_for('auth.auth_admin'))

@auth.route('/cadastro')
def signup():
    return render_template("auth/cadastro.html")

@auth.route('/signup_post', methods=['POST'])
def signup_post():
    email = request.form.get("email", None)
    name = request.form.get("name", None)
    username = request.form.get("username", None)
    password = request.form.get("password", None)

    user = User.query.filter_by(email=email).first()

    if user: 
        return redirect(url_for('auth.signup'))

    new_user = User(email=email, name=name, username=username,  password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))