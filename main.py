from flask import Flask
from routes.api_routes import apiRoutes
from data.env import POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT
import database.postgres  # Initializes global postgres connection
from init.initialize import initialize  # Import the initialize function

app = Flask(__name__)
app.register_blueprint(apiRoutes, url_prefix="/api/v1")

@app.route('/')
def home():
    return "Server is running!"

if __name__ == "__main__":
    # Initialize the database before starting the server
    initialize()
    
    # Run the Flask development server
    app.run(host="0.0.0.0", port=8000, debug=True)
