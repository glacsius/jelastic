from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def config_db(app):
    app.config['BANCODEDADOS'] = 'sqlite:////tmp/test.db'
    db.init_app(app)
    db.create_all(app=app)
