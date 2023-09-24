# Give me a flask basic file 
from flask import Flask

# Create a Flask web application
app = Flask(__name__)

# Define a route for the root URL ("/") that returns "Hello, World!"
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Run the Flask app on the local development server
if __name__ == '__main__':
    app.run()
