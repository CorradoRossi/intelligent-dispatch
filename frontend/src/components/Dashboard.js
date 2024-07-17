import React, { useState, useEffect } from 'react';
import axios from 'axios';

function Dashboard() {
  const [assignments, setAssignments] = useState([]);

  useEffect(() => {
    fetchAssignments();
  }, []);

  const fetchAssignments = async () => {
    try {
      const response = await axios.get('/assignments');
      setAssignments(response.data);
    } catch (error) {
      console.error('Error fetching assignments:', error);
    }
  };

  return (
    <div className="Dashboard">
      <h2>Daily Assignments</h2>
      <table>
        <thead>
          <tr>
            <th>Service Request</th>
            <th>Customer</th>
            <th>Technician</th>
            <th>Date</th>
          </tr>
        </thead>
        <tbody>
          {assignments.map(assignment => (
            <tr key={assignment.id}>
              <td>{assignment.service_request.service_type}</td>
              <td>{assignment.service_request.customer.name}</td>
              <td>{assignment.technician.name}</td>
              <td>{assignment.assigned_date}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default Dashboard;