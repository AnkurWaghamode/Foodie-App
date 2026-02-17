from flask import Blueprint, jsonify
from extensions import db
from models.restaurant_model import Restaurant
from models.order_model import Order
from models.feedback_model import Feedback


admin_bp = Blueprint("admin", __name__)

@admin_bp.route("/api/v1/admin/restaurants/<int:restaurant_id>/approve", methods=["PUT"])
def approve_restaurant(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)

    if not restaurant:
        return jsonify({"message": "Restaurant not found"}), 404

    restaurant.is_approved = True
    db.session.commit()

    return jsonify({"message": "Restaurant approved successfully"}), 200

@admin_bp.route("/api/v1/admin/restaurants/<int:restaurant_id>/disable", methods=["PUT"])
def disable_restaurant_admin(restaurant_id):
    restaurant = Restaurant.query.get(restaurant_id)

    if not restaurant:
        return jsonify({"message": "Restaurant not found"}), 404

    restaurant.is_active = False
    db.session.commit()

    return jsonify({"message": "Restaurant disabled by admin"}), 200

@admin_bp.route("/api/v1/admin/orders", methods=["GET"])
def view_all_orders():
    orders = Order.query.all()

    result = []

    for order in orders:
        result.append({
            "order_id": order.id,
            "user_id": order.user_id,
            "restaurant_id": order.restaurant_id,
            "status": order.status
        })

    return jsonify(result), 200

@admin_bp.route("/api/v1/admin/feedback", methods=["GET"])
def view_all_feedback():

    feedbacks = Feedback.query.all()

    result = []

    for fb in feedbacks:
        result.append({
            "feedback_id": fb.id,
            "user_id": fb.user_id,
            "restaurant_id": fb.restaurant_id,
            "rating": fb.rating,
            "comment": fb.comment
        })

    return jsonify(result), 200

