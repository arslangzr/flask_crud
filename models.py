from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class EmployeeModel(db.Model):
    __tablename__ = "employees"  # Changed table name from "table" to something more descriptive

    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer(), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)  # Specify length for VARCHAR
    age = db.Column(db.Integer(), nullable=False)
    position = db.Column(db.String(80), nullable=False)  # Specify length for VARCHAR

    def __init__(self, employee_id, name, age, position):
        self.employee_id = employee_id
        self.name = name
        self.age = age
        self.position = position

    def __repr__(self):
        return f"{self.name}:{self.employee_id}"
