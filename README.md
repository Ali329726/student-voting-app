# Student Voting App

A simple Flask-based Student Voting Application developed to demonstrate basic REST API functionality and Git/GitHub version control.

## Features

- Check application health
- Cast a vote for a candidate
- View voting results
- Reset voting results
- REST API endpoints using Flask

## Technologies Used

- Python
- Flask
- REST API
- Git
- GitHub

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/health` | Checks whether the application is running |
| POST | `/vote/<candidate>` | Casts a vote for a candidate |
| GET | `/results` | Displays the current voting results |
| POST | `/reset` | Resets all voting results |

## Project Structure

```text
student-voting-app/
├── temp/
│   └── screenshots/
├── README.md
└── votingapp.py
```

## Screenshots

Screenshots related to the project and Git/GitHub workflow are stored in the `temp/screenshots` folder.

## How to Run

1. Install Python.
2. Install Flask:

```bash
pip install flask
```

3. Run the application:

```bash
python votingapp.py
```

4. Open the API endpoints in a browser or API client such as Postman.

## Author

Shaik Mohammad Ali
