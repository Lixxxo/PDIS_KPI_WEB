# flask app and routes

from flask import Flask, render_template
# Database
from flask_sqlalchemy import SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI
from Models.models import Expense, Project, Contract
from Database.db import db
from api import api
import json

# create the app
app = Flask(__name__, static_url_path='',
            static_folder='static',
            template_folder='templates')

# settings

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# no cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
db.init_app(app)

app.register_blueprint(api, url_prefix="/api")
SQLAlchemy(app)


@app.route('/')
def index():
    expenses = Expense.query.all()
    table = {
        "headers": ["Monto", "Tipo", "Fecha", "Detalles"],
        "expenses": expenses
    }
    projects = Project.query.all()
    print(projects)
    projects = [p.name for p in projects]

    materials = [e.amount for e in expenses if e.expense_type == "Material"]
    contracts = [e.amount for e in expenses if e.expense_type == "Contrato"]

    chart_json = dict(
        {"materials": materials,
        "contracts": contracts,
        "projects": projects,
    })

    return render_template('index.html', table=table, chart=chart_json)
