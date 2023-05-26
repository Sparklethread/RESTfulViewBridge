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
    # Define the columns based on your Order view structure
    # ...

class Customer(db.Model):
    __tablename__ = 'Customer'
    __table_args__ = {'autoload':True, 'autoload_with':db.engine, 'extend_existing':True}
    # Define the columns based on your Customer view structure
    # ...

class Invoice(db.Model):
    __tablename__ = 'Invoice'
    __table_args__ = {'autoload':True, 'autoload_with':db.engine, 'extend_existing':True}
    # Define the columns based on your Invoice view structure
    # ...

@app.route('/Order', methods=['GET'])
@auth.login_required
def get_order():
    try:
        records = Order.query.all()
        # Modify the jsonify part based on your Order view structure
        return jsonify([record.some_field for record in records])
    except Exception as e:
        abort(500, description="Internal Server Error. Error: " + str(e))

@app.route('/Customer', methods=['GET'])
@auth.login_required
def get_customer():
    try:
        records = Customer.query.all()
        # Modify the jsonify part based on your Customer view structure
        return jsonify([record.some_field for record in records])
    except Exception as e:
        abort(500, description="Internal Server Error. Error: " + str(e))

@app.route('/Invoice', methods=['GET'])
@auth.login_required
def get_invoice():
    try:
        records = Invoice.query.all()
        # Modify the jsonify part based on your Invoice view structure
        return jsonify([record.some_field for record in records])
    except Exception as e:
        abort(500, description="Internal Server Error. Error: " + str(e))

if __name__ == '__main__':
    app.run(debug=True)
