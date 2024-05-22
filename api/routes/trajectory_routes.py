"""..."""
from flask import Blueprint, jsonify
from ..models.trajectory import Trajectory

trajectory_bp = Blueprint('trajectory', __name__, url_prefix='/trajectories')

@trajectory_bp.route('/', methods=['GET'])
def get_trajectories(id, date):
    """..."""
    # Assuming Trajectory model and to_dict method are defined and imported
    trajectories = Trajectory.query.all()
    return jsonify([trajectory.to_dict() for trajectory in trajectories])
