"""..."""
from api.__init__ import db

class Taxi(db.Model):
    """..."""
    __tablename__ = 'taxis'  # Specify the actual table name here
    id = db.Column(db.Integer, primary_key=True)
    plate = db.Column(db.String(255), nullable=False)
    trajectories = db.relationship('Trajectory', backref='taxi', lazy=True)

    def to_dict(self):
        """..."""
        return {"id": self.id, 
                "plate": self.plate
                }
