from app import db

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
