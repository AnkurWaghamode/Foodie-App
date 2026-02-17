from extensions import db

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("user_tests.robot.id"),
        nullable=False
    )

    restaurant_id = db.Column(
        db.Integer,
        db.ForeignKey("restaurant.id"),
        nullable=False
    )

    status = db.Column(db.String(50), default="Placed")
