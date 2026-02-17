from flask import Blueprint, request, jsonify
from extensions import db
from models.user_model import User
from werkzeug.security import generate_password_hash, check_password_hash
from models.feedback_model import Feedback
from models.restaurant_model import Restaurant


user_bp = Blueprint("user", __name__)

@user_bp.route("/api/v1/users/register", methods=["POST"])
def register_user():
    data = request.get_json()

    if not data.get("email") or not data.get("password"):
        return jsonify({"message": "Email and password required"}), 400

    existing_user = User.query.filter_by(email=data["email"]).first()

    if existing_user:
        return jsonify({"message": "User already exists"}), 409

    hashed_password = generate_password_hash(data["password"])

    new_user = User(
        name=data.get("name"),
        email=data["email"],
        password=hashed_password
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

@user_bp.route("/api/v1/users/login", methods=["POST"])
def login_user():
    data = request.get_json()

    user = User.query.filter_by(email=data.get("email")).first()

    if not user or not check_password_hash(user.password, data.get("password")):
        return jsonify({"message": "Invalid credentials"}), 401

    return jsonify({
        "message": "Login successful",
        "user_id": user.id,
        "email": user.email
    }), 200

@user_bp.route("/api/v1/users/<int:user_id>/feedback", methods=["POST"])
def give_feedback(user_id):

    data = request.get_json()

    restaurant = Restaurant.query.get(data.get("restaurant_id"))

    if not restaurant:
        return jsonify({"message": "Restaurant not found"}), 404

    if not (1 <= data.get("rating") <= 5):
        return jsonify({"message": "Rating must be between 1 and 5"}), 400

    feedback = Feedback(
        user_id=user_id,
        restaurant_id=data["restaurant_id"],
        rating=data["rating"],
        comment=data.get("comment")
    )

    db.session.add(feedback)
    db.session.commit()

    return jsonify({"message": "Feedback submitted successfully"}), 201
