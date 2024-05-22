"""..."""
from unittest.mock import patch, MagicMock
import pytest
from flask import json, url_for
from ..api.__init__ import create_app
from ..api.models.taxi import Taxi

@pytest.fixture
def client():
    """..."""
    app = create_app()
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_get_taxis_no_taxis(client):
    """..."""
    with patch('..models.taxi.Taxi.query') as mock_query:
        mock_paginate = MagicMock()
        mock_query.paginate.return_value = mock_paginate
        mock_paginate.items = []
        mock_paginate.has_next = False
        mock_paginate.has_prev = False
        mock_paginate.pages = 0

        response = client.get(url_for('taxi.get_taxis'))
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['taxis'] == []
        assert data['next_url'] is None
        assert data['prev_url'] is None
        assert data['total_pages'] == 0

def test_get_taxis_with_taxis(client):
    """..."""
    with patch('..models.taxi.Taxi.query') as mock_query:
        mock_paginate = MagicMock()
        mock_query.paginate.return_value = mock_paginate
        mock_paginate.items = [MagicMock(to_dict=lambda: {'id': 1, 'name': 'Taxi 1'})]
        mock_paginate.has_next = True
        mock_paginate.has_prev = False
        mock_paginate.pages = 10
        mock_paginate.next_num = 2

        response = client.get(url_for('taxi.get_taxis'))
        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data['taxis']) == 1
        assert data['taxis'][0] == {'id': 1, 'name': 'Taxi 1'}
        assert data['next_url'] == url_for('taxi.get_taxis', page=2)
        assert data['prev_url'] is None
        assert data['total_pages'] == 10
