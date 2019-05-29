from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def config_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data/aks.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    db.init_app(app)
    db.create_all(app=app)


def add_obj(obj):
    db.session.add(obj)
    db.session.commit()


def delete_obj(obj):
    db.session.delete(obj)
    db.session.commit()


def maior(campo):
    res = db.session.query(db.func.max(campo)).scalar()
    return int(res)
