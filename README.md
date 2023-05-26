RESTfulViewBridge
----------------------------------------------------------------------
RESTfulViewBridge is a Python-based REST API that provides a simple and secure bridge to SQL views. Built on Flask and SQLAlchemy, it provides an easy way to expose your SQL views through a RESTful API, while ensuring secure access via HTTP basic authentication.
----------------------------------------------------------------------
Installation
Make sure you have Python 3.6 or later installed.
----------------------------------------------------------------------
Clone the repository:
git clone https://github.com/Sparklethread/RESTfulViewBridge.git
----------------------------------------------------------------------
Install the required packages: pip install -r requirements.txt
----------------------------------------------------------------------
Replace the database URI, username, and password in app.config['SQLALCHEMY_DATABASE_URI'] with your actual SQL Server credentials.

Define SQLAlchemy models for your SQL views in the script.
----------------------------------------------------------------------
Usage
Start the server: python app.py
----------------------------------------------------------------------
Send a GET request to the API: curl -u username:password http://localhost:5000/your_view
----------------------------------------------------------------------

Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
----------------------------------------------------------------------
License
MIT
----------------------------------------------------------------------

Replace username:password and http://localhost:5000/your_view with the actual username, password, and API endpoint.
