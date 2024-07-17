from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/intelligent_dispatch'
db = SQLAlchemy(app)

# Import models
from models import Customer, Technician, ServiceRequest, TechnicianAvailability, Assignment

@app.route('/service-requests', methods=['POST'])
def create_service_request():
    data = request.json
    new_request = ServiceRequest(
        customer_id=data['customer_id'],
        service_type=data['service_type'],
        description=data['description'],
        requested_date=datetime.strptime(data['requested_date'], '%Y-%m-%d').date()
    )
    db.session.add(new_request)
    db.session.commit()
    return jsonify({'message': 'Service request created successfully', 'id': new_request.id}), 201

@app.route('/service-requests', methods=['GET'])
def get_service_requests():
    requests = ServiceRequest.query.all()
    return jsonify([request.to_dict() for request in requests])

@app.route('/technician-availability', methods=['POST'])
def update_technician_availability():
    data = request.json
    availability = TechnicianAvailability(
        technician_id=data['technician_id'],
        date=datetime.strptime(data['date'], '%Y-%m-%d').date(),
        is_available=data['is_available']
    )
    db.session.add(availability)
    db.session.commit()
    return jsonify({'message': 'Technician availability updated successfully'}), 200

@app.route('/assign-technician', methods=['POST'])
def assign_technician():
    data = request.json
    service_request = ServiceRequest.query.get(data['service_request_id'])
    technician = find_available_technician(service_request)
    
    if technician:
        assignment = Assignment(
            service_request_id=service_request.id,
            technician_id=technician.id,
            assigned_date=service_request.requested_date
        )
        db.session.add(assignment)
        service_request.status = 'assigned'
        db.session.commit()
        return jsonify({'message': 'Technician assigned successfully', 'technician_id': technician.id}), 200
    else:
        return jsonify({'message': 'No available technician found'}), 404

def find_available_technician(service_request):
    # Simple matching algorithm
    available_technicians = Technician.query.join(TechnicianAvailability).filter(
        TechnicianAvailability.date == service_request.requested_date,
        TechnicianAvailability.is_available == True
    ).all()
    
    # For MVP, just return the first available technician
    # In a real-world scenario, you'd consider factors like location, skills, etc.
    return available_technicians[0] if available_technicians else None

if __name__ == '__main__':
    app.run(debug=True)