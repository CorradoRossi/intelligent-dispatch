import React, { useState } from 'react';
import axios from 'axios';

function ServiceRequestForm() {
  const [formData, setFormData] = useState({
    customer_id: '',
    service_type: '',
    description: '',
    requested_date: '',
  });

  const handleChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      await axios.post('/service-requests', formData);
      alert('Service request created successfully!');
      setFormData({
        customer_id: '',
        service_type: '',
        description: '',
        requested_date: '',
      });
    } catch (error) {
      console.error('Error creating service request:', error);
      alert('Failed to create service request');
    }
  };

  return (
    <div className="ServiceRequestForm">
      <h2>Create Service Request</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="customer_id">Customer ID:</label>
          <input
            type="number"
            id="customer_id"
            name="customer_id"
            value={formData.customer_id}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label htmlFor="service_type">Service Type:</label>
          <input
            type="text"
            id="service_type"
            name="service_type"
            value={formData.service_type}
            onChange={handleChange}
            required
          />
        </div>
        <div>
          <label htmlFor="description">Description:</label>
          <textarea
            id="description"
            name="description"
            value={formData.description}
            onChange={handleChange}
            required
          ></textarea>
        </div>
        <div>
          <label htmlFor="requested_date">Requested Date:</label>
          <input
            type="date"
            id="requested_date"
            name="requested_date"
            value={formData.requested_date}
            onChange={handleChange}
            required
          />
        </div>
        <button type="submit">Create Request</button>
      </form>
    </div>
  );
}

export default ServiceRequestForm;