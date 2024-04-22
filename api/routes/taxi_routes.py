"""..."""
from flask import Blueprint, jsonify, url_for, request
from ..models.taxi import Taxi

taxi_bp = Blueprint('taxi', __name__, url_prefix='/taxis')

ROWS_PER_PAGE = 10

@taxi_bp.route('/', methods=['GET'])
def get_taxis():
    """..."""
    page = request.args.get('page', 1, type=int)
    paginated_taxis = Taxi.query.paginate(page=page, per_page=ROWS_PER_PAGE)
    # Assuming Taxi model and to_dict method are defined and imported

    taxis = [taxi.to_dict() for taxi in paginated_taxis.items]
    next_url = url_for('taxi.get_taxis', page=paginated_taxis.next_num) \
        if paginated_taxis.has_next else None
    prev_url = url_for('taxi.get_taxis', page=paginated_taxis.prev_num) \
        if paginated_taxis.has_prev else None

    return jsonify({
        'taxis': taxis,
        'next_url': next_url,
        'prev_url': prev_url,
        'total_pages': paginated_taxis.pages,
        'current_page': page
    })


    #--------------------------------------------------

    #taxis = Taxi.query.all()
    #taxis_json = [taxi.to_dict() for taxi in taxis]
    #return jsonify(taxis_json)
