from flask import Blueprint, render_template
from apps.app import db
from apps.order.forms import Vegetable
from apps.crud.models import User
from flask import Blueprint, render_template, flash, url_for, redirect, request
from flask_login import login_user, logout_user
from apps.crud.models import User


order = Blueprint(
    "order",
    __name__,
    template_folder="templates",
    static_folder="static"
)
@order.route("/")
def index():
    return render_template("order/index.html")

@order.route("/orders",methods = ["GET","POST"])
def orders():
    form = Vegetable()
    if form.validate_on_submit():
        user = User(
            gar = form.gar.data,
            car = form.car.data,
            oni = form.oni.data,
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("crud.user"))
    return render_template("order/wallet.html",form = form)