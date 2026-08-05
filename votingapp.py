from flask import Flask, jsonify

app = Flask(__name__)

# Store votes
votes = {}

@app.route("/")
def home():
    return """
    <h1>Student Voting Application</h1>
    <h3>Your application is running successfully! ✅</h3>

    <p><b>Available Endpoints:</b></p>
    <ul>
        <li>/health - Check application status</li>
        <li>/vote/&lt;candidate&gt; - Cast a vote</li>
        <li>/results - View voting results</li>
        <li>/reset - Reset all votes</li>
    </ul>
    """

@app.route("/health")
def health():
    return "Application is running successfully."

@app.route("/vote/<candidate>")
def vote(candidate):
    votes[candidate] = votes.get(candidate, 0) + 1
    return f"Vote recorded successfully for {candidate}"

@app.route("/results")
def results():
    return jsonify(votes)

@app.route("/reset")
def reset():
    votes.clear()
    return "All votes have been reset successfully."

if __name__ == "__main__":
    app.run(debug=True)
    
