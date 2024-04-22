"""..."""
from flask import Blueprint, jsonify
from ..models.taxi import Taxi

taxi_bp = Blueprint('taxi', __name__, url_prefix='/taxis')

@taxi_bp.route('/', methods=['GET'])
def get_taxis():
    """..."""
    # Assuming Taxi model and to_dict method are defined and imported
    taxis = Taxi.query.all()
    taxis_json = [taxi.to_dict() for taxi in taxis]
    return jsonify(taxis_json)
