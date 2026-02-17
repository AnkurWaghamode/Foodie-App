from extensions import db

class Dish(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50))
    price = db.Column(db.Float, nullable=False)
    available_time = db.Column(db.String(50))
    image = db.Column(db.String(200))
    is_available = db.Column(db.Boolean, default=True)

    restaurant_id = db.Column(
        db.Integer,
        db.ForeignKey("restaurant.id"),
        nullable=False
    )
