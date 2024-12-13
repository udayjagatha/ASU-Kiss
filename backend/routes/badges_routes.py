from flask import Blueprint, jsonify, session
import mysql.connector

# Create a blueprint for badges routes
badges_blueprint = Blueprint("badges", __name__)

# Database Configuration
DB_CONFIG = {
    "host": "localhost",
    "database": "STUDENT",      # Your database name
    "user": "root",             # Your MySQL username
    "password": "Puppy$7677",   # Your MySQL password
    "port": 3306                # Default MySQL port
}


def get_db_connection():
    try:
        return mysql.connector.connect(**DB_CONFIG)
    except mysql.connector.Error as e:
        raise Exception(f"Database connection error: {e}")


# Complete Badge Data
badge_data_list = [
    {
        "category": "Initiative",
        "title": "Initiative",
        "image": "/static/Initiative/Initiative.png",
        "secondaryImage": "/static/Initiative/Initiative back.png"
    },
    {
        "category": "Endurance",
        "title": "Endurance",
        "image": "/static/Endurance/Endurance.png",
        "secondaryImage": "/static/Endurance/Endurance both back.png"
    },
    {
        "category": "Endurance",
        "title": "Endurance (one star - left)",
        "image": "/static/Endurance/Endurance (one star - left).png",
        "secondaryImage": "/static/Endurance/Endurance (one star - left) back .png"
    },
    {
        "category": "Endurance",
        "title": "Endurance (one star - right)",
        "image": "/static/Endurance/Endurance (one star - right).png",
        "secondaryImage": "/static/Endurance/Endurance (one star - right) back.png"
    },
    {
        "category": "Commitment",
        "title": "Commitment badge (1 star)",
        "image": "/static/Commitment/Commitment badge (1 star).png",
        "secondaryImage": "/static/Commitment/Commitment badge (1 star) back.png"
    },
    {
        "category": "Commitment",
        "title": "Commitment badge (2 stars)",
        "image": "/static/Commitment/Commitment badge (2 stars).png",
        "secondaryImage": "/static/Commitment/Commitment badge (2 stars) back.png"
    },
    {
        "category": "Commitment",
        "title": "Commitment badge (3 stars)",
        "image": "/static/Commitment/Commitment badge (3 stars).png",
        "secondaryImage": "/static/Commitment/Commitment badge (3 stars) back.png"
    },
    {
        "category": "Commitment",
        "title": "Commitment badge (4 stars)",
        "image": "/static/Commitment/Commitment badge (4 stars).png",
        "secondaryImage": "/static/Commitment/Commitment badge (4 stars) back.png"
    },
    {
        "category": "Determination",
        "title": "Determination",
        "image": "/static/Determination/Determination.png",
        "secondaryImage": "/static/Determination/Determination back.png"
    },
    {
        "category": "Exertion",
        "title": "Exertion",
        "image": "/static/Exertion/Exertion.png",
        "secondaryImage": "/static/Exertion/Exertion back.png"
    },
    {
        "category": "Community",
        "title": "Community",
        "image": "/static/Community/Community.png",
        "secondaryImage": "/static/Community/Community back.png"
    },
]

# Create a dictionary for easy lookup by title
badge_data_dict = {badge['title']: badge for badge in badge_data_list}


# # Route: Fetch Badges for the Logged-in User
# @badges_blueprint.route("/badges", methods=["GET"])
# def get_badges():
#     conn = None
#     cur = None
#     try:
#         # Get the username from the session
#         username = session.get('username')
#         if not username:
#             return jsonify({"message": "User not logged in"}), 401

#         # Connect to the database
#         conn = get_db_connection()
#         cur = conn.cursor(dictionary=True)

#         # Query to get badges for the user
#         cur.execute("""
#             SELECT
#                 Id AS id,
#                 badgename
#             FROM BADGES
#             WHERE username = %s
#         """, (username,))
#         user_badges = cur.fetchall()

#         # Prepare the response data
#         badges_list = []
#         for badge in user_badges:
#             # Split the badgename field into individual badge titles
#             badgenames = badge['badgename'].split(", ")
#             for badgename in badgenames:
#                 # Match the badge name with predefined badge data
#                 badge_info = badge_data_dict.get(badgename)
#                 if badge_info:
#                     badge_entry = {
#                         "id": badge["id"],
#                         "title": badge_info["title"],
#                         "category": badge_info["category"],
#                         "image": badge_info["image"],
#                         "secondaryImage": badge_info["secondaryImage"]
#                     }
#                     badges_list.append(badge_entry)
#                 else:
#                     # Handle missing badge data
#                     print(f"Badge '{badgename}' not found in badge data.")
#                     # Optionally include minimal badge info or skip
#                     badge_entry = {
#                         "id": badge["id"],
#                         "title": badgename,
#                         "category": "Unknown",
#                         "image": "/static/default.png",               # Default image path
#                         "secondaryImage": "/static/default_back.png"  # Default secondary image path
#                     }
#                     badges_list.append(badge_entry)

#         response_data = {
#             "badges": badges_list
#         }

#         return jsonify(response_data), 200

#     except mysql.connector.Error as e:
#         print(f"Database error: {e}")
#         return jsonify({"message": "Database error", "error": str(e)}), 500

#     except Exception as ex:
#         print(f"An error occurred: {ex}")
#         return jsonify({"message": "An unexpected error occurred", "error": str(ex)}), 500

#     finally:
#         # Safely close cursor and connection
#         if cur:
#             cur.close()
#         if conn:
#             conn.close()
#         print("Database connection closed")

@badges_blueprint.route("/badges", methods=["GET"])
def get_badges():
    conn = None
    cur = None
    try:
        # Get the username from the session
        username = session.get('username')
        if not username:
            return jsonify({"message": "User not logged in"}), 401

        # Connect to the database
        conn = get_db_connection()
        cur = conn.cursor(dictionary=True)

        # Query to get badges for the user
        cur.execute("""
            SELECT
                Id AS id,
                badgename
            FROM BADGES
            WHERE username = %s
        """, (username,))
        user_badges = cur.fetchall()

        # Prepare the response data
        badge_count_map = {}
        for badge in user_badges:
            # Split the badgename field into individual badge titles
            badgenames = badge['badgename'].split(", ")
            for badgename in badgenames:
                # Check if the badge already exists in the map
                if badgename in badge_count_map:
                    # Increase the trophy count for existing badges
                    badge_count_map[badgename]['trophyCount'] += 1
                else:
                    # Match the badge name with predefined badge data
                    badge_info = badge_data_dict.get(badgename)
                    if badge_info:
                        # Add the badge to the map with a trophy count of 1
                        badge_count_map[badgename] = {
                            "id": badge["id"],
                            "title": badge_info["title"],
                            "category": badge_info["category"],
                            "image": badge_info["image"],
                            "secondaryImage": badge_info["secondaryImage"],
                            "trophyCount": 1
                        }
                    else:
                        # Handle missing badge data
                        print(f"Badge '{badgename}' not found in badge data.")
                        # Add default badge info with a trophy count of 1
                        badge_count_map[badgename] = {
                            "id": badge["id"],
                            "title": badgename,
                            "category": "Unknown",
                            "image": "/static/default.png",               # Default image path
                            "secondaryImage": "/static/default_back.png", # Default secondary image path
                            "trophyCount": 1
                        }

        # Convert the badge map to a list for the response
        badges_list = list(badge_count_map.values())

        response_data = {
            "badges": badges_list
        }

        return jsonify(response_data), 200

    except mysql.connector.Error as e:
        print(f"Database error: {e}")
        return jsonify({"message": "Database error", "error": str(e)}), 500

    except Exception as ex:
        print(f"An error occurred: {ex}")
        return jsonify({"message": "An unexpected error occurred", "error": str(ex)}), 500

    finally:
        # Safely close cursor and connection
        if cur:
            cur.close()
        if conn:
            conn.close()
        print("Database connection closed")
