from flask import Flask
from pathlib import Path
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():

    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY = "2fqfaf5286478",
        SQLALCHEMY_DATABASE_URI = f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}",
        SQLALCHEMY_TRACK_MODIFICATIONS=False
    )

    db.init_app(app)
    Migrate(app,db)

    from apps.crud import views as crud_views

    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    return app


"""
app.config["SECRET_KEY"] = "151135gbibib"
app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER")
app.config["MAIL_PORT"] = os.environ.get("MAIL_PORT")
app.config["MAIL_USE_TLS"] = os.environ.get("MAIL_USE_TLS")
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER")

mail = Mail(app)

@app.route("/")
def index():
    return "Hello, Flaskbook!"

@app.route("/hello/<name>",
           methods=["GET"],
           endpoint="hello-endpoint")
def hello(name):
    return f"Hello,{name}!"

@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html",name=name)

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/contact/complete",methods=["GET","POST"])
def contact_complete():
    if request.method == "POST":

        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]

        is_valid = True

        if not username:
            flash("사용자명은 필수입니다.")
            is_valid = False
        
        if not email:
            flash("메일 주소는 필수입니다.")
            is_valid = False

        try:
            validate_email(email)
        except EmailNotValidError:
            flash("메일 주소의 형식으로 입력해 주세요")
            is_valid = False
        
        if not description:
            flash("문의 내용은 필수 입니다.")
            is_valid = False

        if not is_valid:
            return redirect(url_for("contact"))
        
        
        send_email(email,"문의 감사합니다.","contact_mail",username = username, description = description)
        
        flash("문의해 주셔서 감사합니다.")

        

        return redirect(url_for("contact_complete"))
    
    return render_template("contact_complete.html")

def send_email(to,subject,template,**kwargs):
    msg = Message(subject,recipients=[to])
    msg.body = render_template(template + ".txt",**kwargs)
    msg.html = render_template(template + ".html", **kwargs)
    mail.send(msg)
"""
'''
def create_app():
    app = Flask(__name__)
    from apps.crud import views as crud_views

    app.register_blueprint(crud_views.crud,url_prefix="/crud")

    return app
'''
"""
with app.test_request_context():
    print(url_for("index"))
    print(url_for("hello-endpoint",name = "world"))
    print(url_for("show_name",name="AK",page="1"))
    print(url_for("contact"))
"""

