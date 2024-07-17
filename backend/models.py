from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class Customer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    address = db.Column(db.Text)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'address': self.address
        }

class Technician(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    skills = db.Column(db.ARRAY(db.String))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'phone': self.phone,
            'skills': self.skills
        }

class ServiceRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_id = db.Column(db.Integer, db.ForeignKey('customer.id'), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    requested_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(20), default='pending')

    customer = db.relationship('Customer', backref=db.backref('service_requests', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'customer_id': self.customer_id,
            'service_type': self.service_type,
            'description': self.description,
            'requested_date': self.requested_date.isoformat(),
            'status': self.status
        }

class TechnicianAvailability(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    technician_id = db.Column(db.Integer, db.ForeignKey('technician.id'), nullable=False)
    date = db.Column(db.Date, nullable=False)
    is_available = db.Column(db.Boolean, default=True)

    technician = db.relationship('Technician', backref=db.backref('availabilities', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'technician_id': self.technician_id,
            'date': self.date.isoformat(),
            'is_available': self.is_available
        }

class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    service_request_id = db.Column(db.Integer, db.ForeignKey('service_request.id'), nullable=False)
    technician_id = db.Column(db.Integer, db.ForeignKey('technician.id'), nullable=False)
    assigned_date = db.Column(db.Date, nullable=False)

    service_request = db.relationship('ServiceRequest', backref=db.backref('assignments', lazy=True))
    technician = db.relationship('Technician', backref=db.backref('assignments', lazy=True))

    def to_dict(self):
        return {
            'id': self.id,
            'service_request_id': self.service_request_id,
            'technician_id': self.technician_id,
            'assigned_date': self.assigned_date.isoformat()
        }