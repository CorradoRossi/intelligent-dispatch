import React, { useState, useEffect } from 'react';
import axios from 'axios';

function TechnicianSchedule() {
  const [schedules, setSchedules] = useState([]);

  useEffect(() => {
    fetchTechnicianSchedules();
  }, []);

  const fetchTechnicianSchedules = async () => {
    try {
      const response = await axios.get('/technician-schedules');
      setSchedules(response.data);
    } catch (error) {
      console.error('Error fetching technician schedules:', error);
    }
  };

  return (
    <div className="TechnicianSchedule">
      <h2>Technician Schedules</h2>
      {schedules.map(schedule => (
        <div key={schedule.technician.id} className="schedule-item">
          <h3>{schedule.technician.name}</h3>
          <ul>
            {schedule.assignments.map(assignment => (
              <li key={assignment.id}>
                {assignment.service_request.service_type} - {assignment.assigned_date}
              </li>
            ))}
          </ul>
        </div>
      ))}
    </div>
  );
}

export default TechnicianSchedule;