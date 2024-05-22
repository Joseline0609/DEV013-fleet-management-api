"""Create Taxi Routes"""
from flask import Blueprint, jsonify, url_for, request
from ..models.taxi import Taxi

taxi_bp = Blueprint('taxi', __name__, url_prefix='/taxis')

ROWS_PER_PAGE = 10

def paginate_query(query, page, per_page):
    """Paginate a SQLAlchemy query."""
    paginated_obj = query.paginate(page=page, per_page=per_page)
    next_url = url_for(request.endpoint, page=paginated_obj.next_num) \
        if paginated_obj.has_next else None
    prev_url = url_for(request.endpoint, page=paginated_obj.prev_num) \
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


@taxi_bp.route('/', methods=['GET'])
def get_taxis():
    """List all taxis with pagination."""
    page = request.args.get('page', 1, type=int)
    query = Taxi.query

    taxis, next_url, prev_url, total_pages = paginate_query(query, page, ROWS_PER_PAGE)
    taxis_dicts = [taxi.to_dict() for taxi in taxis]

    return create_response(taxis_dicts, next_url, prev_url, total_pages, page)
