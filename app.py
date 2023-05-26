from flask import Flask, jsonify, abort
from flask_sqlalchemy import SQLAlchemy
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://myusername:mypassword@myhostname/LTDS?driver=SQL+Server'
db = SQLAlchemy(app)

auth = HTTPBasicAuth()

users = {
    "user1": generate_password_hash("password1"),
    "user2": generate_password_hash("password2"),
    # add more users if needed
}

@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username

class Order(db.Model):
    __tablename__ = 'Order'
    __table_args__ = {'autoload':True, 'autoload_with':db.engine, 'extend_existing':True}
    OrderID = db.Column(db.Integer, primary_key=True)
    CustomerID = db.Column(db.Integer)
    OrderDate = db.Column(db.DateTime)
    TotalAmount = db.Column(db.Float)

class Customer(db.Model):
    __tablename__ = 'Customer'
    __table_args__ = {'autoload':True, 'autoload_with':db.engine, 'extend_existing':True}
    CustomerID = db.Column(db.Integer, primary_key=True)
    FirstName = db.Column(db.String(50))
    LastName = db.Column(db.String(50))
    Email = db.Column(db.String(120))
    Phone = db.Column(db.String(20))

class Invoice(db.Model):
    __tablename__ = 'Invoice'
    __table_args__ = {'autoload':True, 'autoload_with':db.engine, 'extend_existing':True}
    InvoiceID = db.Column(db.Integer, primary_key=True)
    OrderID = db.Column(db.Integer)
    InvoiceDate = db.Column(db.DateTime)
    TotalAmount = db.Column(db.Float)
    PaymentStatus = db.Column(db.String(20))

@app.route('/Order', methods=['GET'])
@auth.login_required
def get_order():
    try:
        records = Order.query.all()
        return jsonify([{ 'OrderID': record.OrderID, 'CustomerID': record.CustomerID, 'OrderDate': record.OrderDate, 'TotalAmount': record.TotalAmount } for record in records])
    except Exception as e:
        abort(500, description="Internal Server Error. Error: " + str(e))

@app.route('/Customer', methods=['GET'])
@auth.login_required
def get_customer():
    try:
        records = Customer.query.all()
        return jsonify([{ 'CustomerID': record.CustomerID, 'FirstName': record.FirstName, 'LastName': record.LastName, 'Email': record.Email, 'Phone': record.Phone } for record in records])
    except Exception as e:
        abort(500, description="Internal Server Error. Error: " + str(e))

@app.route('/Invoice', methods=['GET'])
@auth.login_required
def get_invoice():
    try:
        records = Invoice.query.all()
        return jsonify([{ 'InvoiceID': record.InvoiceID, 'OrderID': record.OrderID, 'InvoiceDate': record.InvoiceDate, 'TotalAmount': record.TotalAmount, 'PaymentStatus': record.PaymentStatus } for record in records])
    except Exception as e:
        abort(500, description="Internal Server Error. Error: " + str(e))

if __name__ == '__main__':
    app.run(debug=True)
