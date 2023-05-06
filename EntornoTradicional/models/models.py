from __future__ import annotations
from flask_sqlalchemy import SQLAlchemy
from marshmallow import fields, Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema , auto_field
from sqlalchemy import Column, Identity
from sqlalchemy import Table
from sqlalchemy import ForeignKey
import datetime
from sqlalchemy.orm import Session

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String())
    passwd = db.Column(db.String())
    token = db.Column(db.String())
    email = db.Column(db.String())

class convertRequest(db.Model):
    __tablename__ = "convert_request"
    id_request = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user = db.Column(db.Integer, db.ForeignKey('user.id'))
    file_origin_path = db.Column(db.String(128))
    file_name = db.Column(db.String(128))
    format_request = db.Column(db.String(128))
    status = db.Column(db.String(128), default='uploaded')
    datereg = db.Column(db.DateTime, default=datetime.datetime.utcnow) 
    file_request_path = db.Column(db.String(128))


class UserSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = User
        include_relationships = True
        load_instance = True
        
    id = fields.String()
    user = fields.String()
    passwd = fields.String()
    token = fields.String()
    email = fields.String()

class ConvertRequestSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = convertRequest
        include_relationships = True
        include_fk = True
        load_instance = True
        
    id_request = fields.String()
    id_user = fields.String()
    file_origin_path = fields.String()
    file_name = fields.String()
    format_request = fields.String()
    status = fields.String()
    datereg = fields.String()

