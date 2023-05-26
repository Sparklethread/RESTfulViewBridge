from flask import Blueprint, jsonify, abort
from app import db, auth
from yourapplication.models import Order, Customer, Invoice

routes_blueprint = Blueprint('routes', __name__)

@routes_blueprint.route('/Order', methods=['GET'])
@auth.login_required
def get_order():
    try:
        records = Order.query.all()
        return jsonify([{ 'OrderID': record.OrderID, 'CustomerID': record.CustomerID, 'OrderDate': record.OrderDate, 'TotalAmount': record.TotalAmount } for record in records])
    except Exception as e:
        abort(500, description="Internal Server Error. Error: " + str(e))

@routes_blueprint.route('/Customer', methods=['GET'])
@auth.login_required
def get_customer():
    try:
        records = Customer.query.all()
        return jsonify([{ 'CustomerID': record.CustomerID, 'FirstName': record.FirstName, 'LastName': record.LastName, 'Email': record.Email, 'Phone': record.Phone } for record in records])
    except Exception as e:
        abort(500, description="Internal Server Error. Error: " + str(e))

@routes_blueprint.route('/Invoice', methods=['GET'])
@auth.login_required
def get_invoice():
    try:
        records = Invoice.query.all()
        return jsonify([{ 'InvoiceID': record.InvoiceID, 'OrderID': record.OrderID, 'InvoiceDate': record.InvoiceDate, 'TotalAmount': record.TotalAmount, 'PaymentStatus': record.PaymentStatus } for record in records])
    except Exception as e:
        abort(500, description="Internal Server Error. Error: " + str(e))
