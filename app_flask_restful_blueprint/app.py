from flask import Flask
from app_flask_restful_blueprint.tudo import blueprint as blu


app = Flask(__name__)
app.register_blueprint(blu)


if __name__ == '__main__':
    app.run(debug=True)
