from flask import Flask
from routes.api_routes import apiRoutes

app = Flask(__name__)
app.register_blueprint(apiRoutes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)