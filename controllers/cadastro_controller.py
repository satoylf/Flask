from flask import Blueprint, render_template, redirect, url_for

cadastro = Blueprint("cadastro", __name__, template_folder="./views/", static_folder='./static/', root_path="./")

