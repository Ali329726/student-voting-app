from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to My Voting Application"

@app.route("/health")
def health():
    return "Application is running successfully."

if __name__ == "__main__":
    app.run(debug=True)