from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from yourapplication.routes import routes_blueprint
from yourapplication.auth import auth

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://myusername:mypassword@myhostname/LTDS?driver=SQL+Server'
db = SQLAlchemy(app)
app.register_blueprint(routes_blueprint)

auth.init_app(app)

if __name__ == '__main__':
    app.run(debug=True)
