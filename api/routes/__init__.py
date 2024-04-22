"""..."""
from api.routes.taxi_routes import taxi_bp
from api.routes.trajectory_routes import trajectory_bp

def init_routes(app):
    """..."""
    app.register_blueprint(taxi_bp)
    app.register_blueprint(trajectory_bp)
