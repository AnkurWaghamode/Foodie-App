from flask import Blueprint, request, jsonify
from extensions import db
from models.dish_model import Dish
from models.restaurant_model import Restaurant

dish_bp = Blueprint("dish", __name__)

@dish_bp.route("/api/v1/restaurants/<int:restaurant_id>/dishes", methods=["POST"])
def add_dish(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)

    if not restaurant:
        return jsonify({"message": "Restaurant not found"}), 404

    data = request.get_json()

    new_dish = Dish(
        name=data["name"],
        type=data.get("type"),
        price=data["price"],
        available_time=data.get("available_time"),
        image=data.get("image"),
        restaurant_id=restaurant_id
    )

    db.session.add(new_dish)
    db.session.commit()

    return jsonify({"message": "Dish added successfully"}), 201

@dish_bp.route("/api/v1/dishes/<int:dish_id>", methods=["GET"])
def get_dish(dish_id):
    dish = Dish.query.get(dish_id)

    if not dish:
        return jsonify({"message": "Dish not found"}), 404

    return jsonify({
        "id": dish.id,
        "name": dish.name,
        "type": dish.type,
        "price": dish.price,
        "available_time": dish.available_time,
        "image": dish.image,
        "is_available": dish.is_available,
        "restaurant_id": dish.restaurant_id
    }), 200

@dish_bp.route("/api/v1/dishes/<int:dish_id>", methods=["PUT"])
def update_dish(dish_id):
    dish = Dish.query.get(dish_id)

    if not dish:
        return jsonify({"message": "Dish not found"}), 404

    data = request.get_json()

    if "name" in data:
        dish.name = data["name"]
    if "type" in data:
        dish.type = data["type"]
    if "price" in data:
        dish.price = data["price"]
    if "available_time" in data:
        dish.available_time = data["available_time"]
    if "image" in data:
        dish.image = data["image"]

    db.session.commit()

    return jsonify({"message": "Dish updated successfully"}), 200

@dish_bp.route("/api/v1/dishes/<int:dish_id>/status", methods=["PUT"])
def change_dish_status(dish_id):
    dish = Dish.query.get(dish_id)

    if not dish:
        return jsonify({"message": "Dish not found"}), 404

    data = request.get_json()

    if "enabled" not in data:
        return jsonify({"message": "Enabled field required"}), 400

    dish.is_available = data["enabled"]
    db.session.commit()

    return jsonify({"message": "Dish status updated"}), 200

@dish_bp.route("/api/v1/dishes/<int:dish_id>", methods=["DELETE"])
def delete_dish(dish_id):
    dish = Dish.query.get(dish_id)

    if not dish:
        return jsonify({"message": "Dish not found"}), 404

    db.session.delete(dish)
    db.session.commit()

    return jsonify({"message": "Dish deleted"}), 200
