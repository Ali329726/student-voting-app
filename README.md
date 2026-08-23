## Student Voting Application

## Project Description

The Student Voting Application is a simple Flask-based application that allows users to vote for candidates, view voting results, and reset all votes.

## Installation and Setup

### Install Python

Make sure Python 3.x is installed.

Check Python:

```bash
python --version
install Flask
pip install flask
Run the Application
python votingapp.py

The application runs at:

http://localhost:5000

API Endpoint Reference
Method	Endpoint	Description
GET	/	Displays the welcome message
GET	/health	Checks whether the application is running
GET	/vote/<candidate>	Records a vote for a candidate
GET	/results	Displays the voting results
GET	/reset	Resets all voting results
Home

Endpoint:

http://localhost:5000/

Response:

Welcome to the App
Health

Endpoint:

http://localhost:5000/health

Response:

App is running
Vote

Endpoint:

http://localhost:5000/vote/Ali

Response:

Vote recorded successfully for Ali
Results

Endpoint:

http://localhost:5000/results

Example response:

Ali: 1
Reset

Endpoint:

http://localhost:5000/reset

Response:

All votes have been reset
Git Workflow

The project uses two Git branches:

dev - development branch
main - stable/final branch

Workflow:

Development
     ↓
dev branch
     ↓
Test application
     ↓
Commit changes
     ↓
Push to GitHub
     ↓
Create Pull Request
     ↓
Merge dev → main
Version History
Version 1
Created the basic Flask application.
Added / endpoint.
Added /health endpoint.
Created Git repository.
Created dev branch.
Pushed the project to GitHub.
Version 2
Added /vote/<candidate> endpoint.
Added /results endpoint.
Added /reset endpoint.
Added vote counting.
Tested the application endpoints.
Updated project screenshots.
Pushed changes to the dev branch.
Merged dev into main.
Screenshots
Application Testing

API Testing

Voting Results

Reset Testing

GitHub Workflow

Project Structure
student-voting-app/
├── screenshots/
│   ├── Screenshot (150).png
│   ├── Screenshot (151).png
│   ├── Screenshot (152).png
│   ├── Screenshot (153).png
│   └── Screenshot (154).png
├── README.md
└── votingapp.py
Technologies Used
Python
Flask
REST API
Git
GitHub
Author

Shaik Mohammad Ali

