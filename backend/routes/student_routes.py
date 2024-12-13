from flask import Blueprint, jsonify, session
import mysql.connector

# Create a blueprint for student routes
student_blueprint = Blueprint("students", __name__)

# Database Configuration
DB_CONFIG = {
    "host": "localhost",
    "database": "STUDENT",  # Your database name
    "user": "root",         # Your MySQL username
    "password": "Puppy$7677",  # Your MySQL password
    "port": 3306            # Default MySQL port
}

# Helper function to get a database connection
def get_db_connection():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except mysql.connector.Error as e:
        raise Exception(f"Database connection error: {e}")

# Static student data
default_student_data = {
    "current_streak": 5,
    "longest_streak": 7,
     
    "badges": [
        {
            "title": "Initiative",
            "description": "Initiative means taking action and leading the way, even when it is difficult. Initiative is important because it can help you build self-esteem.",
            "count": 3,
            "last_earned": "10/13/2024",
            "image": "/static/Initiative/initiative.png",
            "secondaryImage": "/static/Initiative/initiative_back.png"
        },
        {
            "title": "Endurance",
            "description": "Endurance means setting goals and having the confidence and stamina to see them through. Endurance is important because it can help you achieve your larger goals.",
            "count": 2,
            "last_earned": "10/15/2024",
            "image": "/static/Endurance/endurance.png",
            "secondaryImage": "/static/Endurance/endurance_back.png"
        },
        {
            "title": "Commitment",
            "description": "Commitment means making pledges to achieve goals. Commitment is important because it can be help you maintain your focus.",
            "count": 1,
            "last_earned": "10/12/2024",
            "image": "/static/Commitment/Commitment badge (4 stars).png",
            "secondaryImage": "/static/Commitment/Commitment badge (4 stars) back.png"
        },
        {
            "title": "Determination",
            "description": "Determination means not letting obstacles get in the way of achieving goals. Determination is important because it can help you stay motivated and achieve success.",
            "count": 4,
            "last_earned": "10/11/2024",
            "image": "/static/Determination/determination.png",
            "secondaryImage": "/static/Determination/determination_back.png"
        },
        {
            "title": "Exertion",
            "description": "Exertion means putting effort and hard work into achieving goals. Exertion is important because it can help you grow from pushing yourself farther.",
            "count": 2,
            "last_earned": "10/14/2024",
            "image": "/static/Exertion/exertion.png",
            "secondaryImage": "/static/Exertion/exertion_back.png"
        },
        {
            "title": "Community",
            "description": "Community means cultivating a sense of togetherness with others. Community is important because it can help you feel connected and part of something bigger than yourself.",
            "count": 3,
            "last_earned": "10/16/2024",
            "image": "/static/Community/community.png",
            "secondaryImage": "/static/Community/community_back.png"
        },
    ]
}

# Route: Fetch Student Data (Protected)
@student_blueprint.route("/student", methods=["GET"])
def get_student_data():
    # Check if the user is logged in'
    
    if "username" not in session:
       
        return jsonify({"message": "Unauthorized. Please log in."}), 401

    username = session["username"]  # Get the logged-in username from the session
   
    session.permanent = True

    # Option 1: If you need to verify the username exists in the database
    conn, cur = None, None
    try:
        # Connect to the database
        conn = get_db_connection()
        cur = conn.cursor(dictionary=True)

        # Query to check if the user exists in the CREDENTIALS table
        cur.execute(
            "SELECT username FROM CREDENTIALS WHERE username = %s",
            (username,)
        )
        user_data = cur.fetchone()

        if not user_data:
            print("User not found in CREDENTIALS table")
            return jsonify({"message": "User not found in the database."}), 404

        # Log successful data fetch for debugging
       # print(f"Fetched data for username: {user_data['username']}")

    except mysql.connector.Error as e:
        print(f"Database error: {e}")
        return jsonify({"message": "Database error", "error": str(e)}), 500

    finally:
        # Safely close cursor and connection
        if cur:
            cur.close()
        if conn:
            conn.close()
        print("Database connection closed")

    # Prepare the response data with the username and static data
    response_data = {
        **default_student_data,
        "name": username,
    }

    return jsonify(response_data), 200
