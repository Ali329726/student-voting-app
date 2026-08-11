from flask import Flask, jsonify

app = Flask(__name__)

# Store votes in memory
votes = {}


# Task 1: Home endpoint
@app.route("/")
def home():
    return "Welcome to the App"


# Task 1: Health endpoint
@app.route("/health")
def health():
    return "App is running"


# Task 3: Vote endpoint
@app.route("/vote/<candidate>")
def vote(candidate):
    votes[candidate] = votes.get(candidate, 0) + 1
    return f"Vote recorded successfully for {candidate}"


# Task 3: Results endpoint
@app.route("/results")
def results():
    if not votes:
        return "No votes recorded"
    
    return "\n".join(f"{candidate}: {count}" for candidate, count in votes.items())

# Task 4: Reset endpoint
@app.route("/reset")
def reset():
    votes.clear()
    return "All votes have been reset"


if __name__ == "__main__":
    app.run(debug=True)