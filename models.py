"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy 
DEFAULT_IMAGE = 'https://tinyurl.com/demo-cupcake'
db = SQLAlchemy()

def connect_db(app):

    db.app = app 
    db.init_app(app)


class Cupcake(db.Model):
    __tablename__ = "cupcake"

    id = db.Column(db.Integer, 
                    primary_key = True,
                    autoincrement = True)
    flavor = db.Column(db.Text,
                        nullable = False)
    size = db.Column(db.Text,
                    nullable = False)
    rating = db.Column(db.Integer,
                        nullable = False)                
    image = db.Column(db.Text,
                    nullable = False,
                    default = DEFAULT_IMAGE)



    def serialize(self):
        return {
            'id': self.id,
            'flavor': self.flavor,
            'size': self.size,
            'rating': self.rating,
            'image': self.image
        }

