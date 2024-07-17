# Intelligent Scheduling and Dispatch

This is an MVP for an Intelligent Scheduling and Dispatch web application for a home services company.

## Prerequisites

- Node.js (v14 or later)
- Python (v3.7 or later)
- PostgreSQL

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/intelligent-dispatch.git
   cd intelligent-dispatch
   ```

2. Set up the backend:
   ```
   cd backend
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

3. Set up the database:
   - Create a PostgreSQL database named `intelligent_dispatch`
   - Update the database connection string in `backend/app.py`
   - Run the SQL commands in `backend/schema.sql` to create the necessary tables

4. Set up the frontend:
   ```
   cd ../frontend
   npm install
   ```

## Running the application locally

1. Start the backend server:
   ```
   cd backend
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   python app.py
   ```

2. In a new terminal, start the frontend development server:
   ```
   cd frontend
   npm start
   ```

3. Open your browser and navigate to `http://localhost:3000`

## Deploying to a server

1. Build the frontend:
   ```
   cd frontend
   npm run build
   ```

2. Copy the contents of the `frontend/build` directory to your web server's public directory.

3. Set up the backend on your server:
   - Install Python and the required packages listed in `requirements.txt`
   - Set up a PostgreSQL database and update the connection string in `app.py`
   - Use a WSGI server like Gunicorn to run the Flask application

4. Configure your web server (e.g., Nginx or Apache) to serve the static files from the frontend build and proxy API requests to the backend server.

## Features

- Create and retrieve service requests
- Update technician availability
- Assign technicians to service requests based on availability
- Display daily assignments and technician schedules

Note: This MVP focuses on core functionality and lacks advanced features like complex scheduling algorithms, user authentication, or real-time updates.

## Database

USER=metastash
PASSWORD=localdbpassword1

## Resources

https://stackoverflow.com/questions/53925660/installing-python-dependencies-locally-in-project
https://www.atlassian.com/data/admin/how-to-start-postgresql-server-on-mac-os-x