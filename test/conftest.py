import pytest
from fixture.main import MainHelper

@pytest.fixture
def app(request):
    fixture = MainHelper()
    request.addfinalizer(fixture.destroy)
    return fixture








