"""..."""
from api.__init__ import db

class Trajectory(db.Model):
    """..."""
    __tablename__ = 'trajectories'  # Specify the actual table name here
    id = db.Column(db.Integer, primary_key=True)
    taxi_id = db.Column(db.Integer, db.ForeignKey('taxis.id'), nullable=False)
    date = db.Column(db.DateTime)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def to_dict(self):
        """..."""
        return {
            "id": self.id, 
            "taxi_id": self.taxi_id, 
            "date": self.date, 
            "latitude": self.latitude, 
            "longitude": self.longitude
        }
