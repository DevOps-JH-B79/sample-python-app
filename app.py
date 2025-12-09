from flask import Flask


# Initiate Flask application
app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Hey, Satish!</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)