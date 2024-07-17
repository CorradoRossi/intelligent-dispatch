import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Dashboard from './components/Dashboard';
import ServiceRequestForm from './components/ServiceRequestForm';
import TechnicianSchedule from './components/TechnicianSchedule';

function App() {
  return (
    <Router>
      <div className="App">
        <header>
          <h1>Intelligent Scheduling and Dispatch</h1>
        </header>
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/create-request" element={<ServiceRequestForm />} />
          <Route path="/technician-schedule" element={<TechnicianSchedule />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;