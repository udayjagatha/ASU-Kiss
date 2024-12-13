from flask import Blueprint, request, jsonify, session
from flask_cors import CORS
import mysql.connector
import bcrypt

# Create Blueprint
auth_blueprint = Blueprint("auth", __name__)

# Enable CORS for this Blueprint
CORS(auth_blueprint, resources={r"/*": {"origins": "http://localhost:3000"}}, supports_credentials=True)

# Database Configuration
DB_CONFIG = {
    "host": "localhost",
    "database": "STUDENT",
    "user": "root",
    "password": "Puppy$7677",
    "port": 3306
}

# Helper function to get a database connection
def get_db_connection():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except mysql.connector.Error as e:
        raise Exception(f"Database connection error: {e}")

# Helper function to safely close resources
def close_resources(conn, cur):
    if cur:
        cur.close()
    if conn:
        conn.close()

# Signup Route
@auth_blueprint.route("/signup", methods=["POST"])
def signup_or_reset_password():
    if not request.is_json:
        return jsonify({"message": "Content-Type must be application/json"}), 415

    # Parse request data
    data = request.json
    username = data.get("username")
    password = data.get("password")

    # Validate input
    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    conn, cur = None, None
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        # Check if the username already exists
        cur.execute("SELECT username FROM CREDENTIALS WHERE username = %s", (username,))
        user = cur.fetchone()

        if user:
            # Reset the password for an existing user
            hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
            cur.execute(
                "UPDATE CREDENTIALS SET password = %s WHERE username = %s",
                (hashed_password.decode("utf-8"), username),
            )
            conn.commit()
            return jsonify({"message": "Password reset successfully"}), 200
        else:
            # Create a new user
            hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
            cur.execute("INSERT INTO CREDENTIALS (username, password) VALUES (%s, %s)",
                        (username, hashed_password.decode("utf-8")))
            conn.commit()
            return jsonify({"message": "User registered successfully"}), 201
    except mysql.connector.Error as e:
        return jsonify({"message": "Database error", "error": str(e)}), 500
    finally:
        close_resources(conn, cur)



@auth_blueprint.route("/login", methods=["POST"])
def login():
    if not request.is_json:
        return jsonify({"message": "Content-Type must be application/json"}), 415

    # Parse request data
    data = request.json
    username = data.get("username")
    password = data.get("password")

    # Validate input
    if not username or not password:
        return jsonify({"message": "Username and password are required"}), 400

    conn, cur = None, None
    try:
        conn = get_db_connection()
        cur = conn.cursor()

        # Check if the username exists and verify the password
        cur.execute("SELECT password FROM CREDENTIALS WHERE username = %s", (username,))
        user = cur.fetchone()
        if user:
            stored_password = user[0]
            if bcrypt.checkpw(password.encode("utf-8"), stored_password.encode("utf-8")):
                # Store username in session
                session["username"] = username
                session.permanent = True  # Make the session persistent
                print(f"Session after login: {session}")
                return jsonify({"message": "Login successful", "username": username}), 200
            else:
                return jsonify({"message": "Invalid password"}), 401
        else:
            return jsonify({"message": "Username not found"}), 404
    except mysql.connector.Error as e:
        return jsonify({"message": "Database error", "error": str(e)}), 500
    finally:
        close_resources(conn, cur)

   
    
        
        
        
        
        
        
        


# Logout Route
@auth_blueprint.route("/logout", methods=["POST"])
def logout():
    if "username" not in session:
        return jsonify({"message": "Unauthorized"}), 401
    session.pop("username", None)  # Remove username from session
    return jsonify({"message": "Logged out successfully"}), 200




