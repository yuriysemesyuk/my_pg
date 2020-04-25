from app import db

class Service(db.Model):
    id_service = db.Column(db.Integer, primary_key=True)
    name_service = db.Column(db.String(20))
    service_time = db.Column(db.String(20))
    prise_service = db.Column(db.String(255))