#-*- coding:utf-8 -*-
# datetime: 2019/3/20 9:25
from sqlalchemy.exc import SQLAlchemyError
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(36), unique=True, nullable=False)
    password = db.Column(db.String(200))
    email = db.Column(db.String(200), unique=True, nullable=False)

    def __repr__(self):
        return 'Users %r' % self.username

    def set_password(self, password):
        return generate_password_hash(password)

    def check_password(self, hash, password):
        return check_password_hash(hash, password)

    def get(self, id):
        return self.query.filter_by(id=id).first()

    def add(self, user):
        db.session.add(user)
        return session_commit()

    def update(self):
        return session_commit()

    def delete(self, id):
        self.query.filter_by(id=id).delete()
        return session_commit()


def session_commit():
    try:
        db.session.commit()
    except SQLAlchemyError as e:
        db.session.rollback()
        reason = str(e)
        return reason