"""..."""
from flask import Blueprint, jsonify, request, url_for
from dateutil import parser
import pytz
from ..models.trajectory import Trajectory
from ..models import db  # Asegúrate de importar db desde tu módulo de modelos

trajectory_bp = Blueprint('trajectory', __name__, url_prefix='/trajectories')

ROWS_PER_PAGE = 10

def paginate_query(query, page, per_page, taxi_id, date_str):
    """Paginate a SQLAlchemy query."""
    paginated_obj = query.paginate(page=page, per_page=per_page)
    next_url = url_for(request.endpoint, taxi_id=taxi_id, date=date_str, page=paginated_obj.next_num) \
        if paginated_obj.has_next else None
    prev_url = url_for(request.endpoint, taxi_id=taxi_id, date=date_str, page=paginated_obj.prev_num) \
        if paginated_obj.has_prev else None

    return paginated_obj.items, next_url, prev_url, paginated_obj.pages


def create_response(data, next_url, prev_url, total_pages, current_page):
    """Create a JSON response for paginated results."""
    return jsonify({
        'data': data,
        'next_url': next_url,
        'prev_url': prev_url,
        'total_pages': total_pages,
        'current_page': current_page
    })


@trajectory_bp.route('/<int:taxi_id>', methods=['GET'])
def get_trajectory_by_taxi(taxi_id):
    """Get latitude, longitude, date, and time for a given taxi and date."""
    date_str = request.args.get('date')

    try:
        # Parse the date string into a datetime object
        date = parser.parse(date_str)
    except ValueError:
        return jsonify({"error": "Invalid date format."}), 400

    # Filter trajectories by taxi_id and date
    query = Trajectory.query.filter(
        Trajectory.taxi_id == taxi_id,
        db.func.date(Trajectory.date) == date.date()
    )

    # Get the first page of trajectories
    page = request.args.get('page', 1, type=int)
    trajectories, next_url, prev_url, total_pages = paginate_query(query, page, ROWS_PER_PAGE, taxi_id, date_str)

    # Create a list of dictionaries with the desired information for each trajectory
    trajectories_data = []
    for trajectory in trajectories:
        trajectory_data = {
            'latitude': trajectory.latitude,
            'longitude': trajectory.longitude,
            'date': trajectory.date.strftime('%Y-%m-%d'),
            'time': trajectory.date.strftime('%H:%M:%S')
        }
        trajectories_data.append(trajectory_data)

    return create_response(trajectories_data, next_url, prev_url, total_pages, page)
