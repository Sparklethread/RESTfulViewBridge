# RESTfulViewBridge

RESTfulViewBridge is a Python-based REST API that provides a simple and secure bridge to SQL views. Built on Flask and SQLAlchemy, it provides an easy way to expose your SQL views through a RESTful API, while ensuring secure access via HTTP basic authentication.

## Installation

1. Make sure you have Python 3.6 or later installed.
2. Clone the repository: `git clone https://github.com/Sparklethread/RESTfulViewBridge.git`
3. Install the required packages: `pip install -r requirements.txt`
4. Replace the database URI, username, and password in `app.config['SQLALCHEMY_DATABASE_URI']` with your actual SQL Server credentials.
5. Define SQLAlchemy models for your SQL views in the script.

## Usage

1. Start the server: `python app.py`
2. Send a GET request to the API:
  curl -u username:password http://localhost:5000/Order
  curl -u username:password http://localhost:5000/Customer
  curl -u username:password http://localhost:5000/Invoice
  Replace `username:password` with your actual username and password.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change. Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
