# from flask import Flask
# from flask_cors import CORS
# from routes.auth_routes import auth_blueprint
# from routes.student_routes import student_blueprint

# app = Flask(__name__)

# # Secret key for session management
# app.secret_key = "11e75106c74fa72d9d5ff543e96d352d3d979a0a46fca0cde50c4a7f8da95450"  # Use a fixed key for development (change for production)

# # Session and cookie settings
# app.config["SESSION_COOKIE_SECURE"] = False  # Allow cookies over HTTP

# app.config["SESSION_COOKIE_SAMESITE"] = "Lax"  # Prevent CSRF attacks while allowing cross-origin

# # Enable CORS for all routes
# CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)

# # Register blueprints
# app.register_blueprint(auth_blueprint, url_prefix="/auth")  # All auth routes prefixed with /auth
# app.register_blueprint(student_blueprint, url_prefix="/api")  # All student routes prefixed with /api

# if __name__ == "__main__":
#     app.run(debug=True)

from flask import Flask
from flask_cors import CORS
from routes.auth_routes import auth_blueprint
from routes.student_routes import student_blueprint
from routes.badges_routes import badges_blueprint  # Import the badges blueprint

app = Flask(__name__)

# Secret key for session management
app.secret_key = "11e75106c74fa72d9d5ff543e96d352d3d979a0a46fca0cde50c4a7f8da95450"  # Replace with a secure key or use environment variables

# Session and cookie settings
app.config["SESSION_COOKIE_SECURE"] = False  # Allow cookies over HTTP
app.config["SESSION_COOKIE_SAMESITE"] = "Lax"  # Prevent CSRF attacks while allowing cross-origin

# Enable CORS for all routes
CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)

# Register blueprints
app.register_blueprint(auth_blueprint, url_prefix="/auth")     # All auth routes prefixed with /auth
app.register_blueprint(student_blueprint, url_prefix="/api")   # All student routes prefixed with /api
app.register_blueprint(badges_blueprint, url_prefix="/api")    # All badges routes prefixed with /api

if __name__ == "__main__":
    app.run(debug=True)
