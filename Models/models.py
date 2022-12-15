from Database.db import db
from datetime import date
import json


class Expense(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    amount = db.Column(db.Integer(), nullable=False)
    type = db.Column(db.String(250), nullable=False)
    date = db.Column(db.Date, default=date.today)
    detail = None

    def __init__(self, amount, expense_type, date, detail):
        self.amount = amount
        self.type = expense_type
        self.date = date
        self.detail = detail

    def to_json(self):
        return {
            'id': self.id,
            'amount': self.amount,
            'type': str(self.type),
            'date': self.date,
            'detail': self.detail
        }


class Material(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), unique=True)
    price = db.Column(db.Integer(), nullable=False)
    quantity = db.Column(db.Integer(), nullable=False)

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity
        }

    @staticmethod
    def from_string(serialized_material: str) -> object:
        json_dct = json.loads(serialized_material)
        return Material(name=json_dct['name'], price=json_dct['price'], quantity=json_dct['quantity'])


class Contract(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    start_date = db.Column(db.Date, default=date.today)
    end_date = db.Column(db.Date, nullable=True)
    salary = db.Column(db.String(250), nullable=False)
    project_name = None

    def __init__(self, salary, project_name):
        self.salary = salary
        self.project_name = project_name

    def to_json(self):
        return {
            'salary': self.salary,
            'project_name': self.project_name
        }

    @staticmethod
    def from_string(serialized_contract: str) -> object:
        json_dct = json.loads(serialized_contract)
        print(json_dct['project']['name'])
        return Contract(salary=json_dct['salary'], project_name=json_dct['project']['name'])


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(250), unique=True)

    def __init__(self, name):
        self.name = name

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name
        }

    @staticmethod
    def from_string(serialized_project: str) -> object:
        json_dct = json.loads(serialized_project)
        return Project(name=json_dct['Name'])
