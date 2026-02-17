from flask import Blueprint, request, jsonify
from extensions import db
from models.restaurant_model import Restaurant

restaurant_bp = Blueprint("restaurant", __name__)

@restaurant_bp.route("/api/v1/restaurants", methods=["POST"])
def register_restaurant():
    data = request.get_json()

    if not data.get("name"):
        return jsonify({"message": "Name is required"}), 400

    new_restaurant = Restaurant(
        name=data["name"],
        category=data["category"],
        location=data["location"],
        contact=data.get("contact")
    )

    db.session.add(new_restaurant)
    db.session.commit()

    return jsonify({"message": "Restaurant created successfully"}), 201

@restaurant_bp.route("/api/v1/restaurants/<int:restaurant_id>", methods=["GET"])
def get_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)

    if not restaurant:
        return jsonify({"message": "Restaurant not found"}), 404

    return jsonify({
        "id": restaurant.id,
        "name": restaurant.name,
        "category": restaurant.category,
        "location": restaurant.location,
        "contact": restaurant.contact,
        "is_active": restaurant.is_active
    }), 200

@restaurant_bp.route("/api/v1/restaurants/<int:restaurant_id>", methods=["PUT"])
def update_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)

    if not restaurant:
        return jsonify({"message": "Restaurant not found"}), 404

    data = request.get_json()

    if "name" in data:
        restaurant.name = data["name"]
    if "category" in data:
        restaurant.category = data["category"]
    if "location" in data:
        restaurant.location = data["location"]
    if "contact" in data:
        restaurant.contact = data["contact"]

    db.session.commit()

    return jsonify({"message": "Restaurant updated successfully"}), 200

@restaurant_bp.route("/api/v1/restaurants/<int:restaurant_id>/disable", methods=["PUT"])
def disable_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)

    if not restaurant:
        return jsonify({"message": "Restaurant not found"}), 404

    restaurant.is_active = False
    db.session.commit()

    return jsonify({"message": "Restaurant disabled"}), 200
