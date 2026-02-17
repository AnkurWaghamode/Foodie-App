from flask import Blueprint, request, jsonify
from extensions import db
from models.order_model import Order
from models.restaurant_model import Restaurant


order_bp = Blueprint("order", __name__)

@order_bp.route("/api/v1/orders", methods=["POST"])
def place_order():
    data = request.get_json()

    user_id = data.get("user_id")
    restaurant_id = data.get("restaurant_id")

    if not user_id or not restaurant_id:
        return jsonify({"message": "User ID and Restaurant ID required"}), 400

    restaurant = Restaurant.query.get(restaurant_id)

    if not restaurant:
        return jsonify({"message": "Restaurant not found"}), 404

    new_order = Order(
        user_id=user_id,
        restaurant_id=restaurant_id
    )

    db.session.add(new_order)
    db.session.commit()

    return jsonify({
        "message": "Order placed successfully",
        "order_id": new_order.id
    }), 201

@order_bp.route("/api/v1/users/<int:user_id>/orders", methods=["GET"])
def view_orders_by_user(user_id):
    orders = Order.query.filter_by(user_id=user_id).all()

    if not orders:
        return jsonify({"message": "No orders found for this user_tests.robot"}), 404

    result = []

    for order in orders:
        result.append({
            "order_id": order.id,
            "restaurant_id": order.restaurant_id,
            "status": order.status
        })

    return jsonify(result), 200

@order_bp.route("/api/v1/restaurants/<int:restaurant_id>/orders", methods=["GET"])
def view_orders_by_restaurant(restaurant_id):
    orders = Order.query.filter_by(restaurant_id=restaurant_id).all()

    if not orders:
        return jsonify({"message": "No orders found for this restaurant"}), 404

    result = []

    for order in orders:
        result.append({
            "order_id": order.id,
            "user_id": order.user_id,
            "status": order.status
        })

    return jsonify(result), 200

@order_bp.route("/api/v1/orders/<int:order_id>", methods=["PUT"])
def update_order_status(order_id):
    order = Order.query.get(order_id)

    if not order:
        return jsonify({"message": "Order not found"}), 404

    data = request.get_json()

    if "status" not in data:
        return jsonify({"message": "Status is required"}), 400

    order.status = data["status"]
    db.session.commit()

    return jsonify({"message": "Order status updated"}), 200

