from pyramid import testing
from pyramid.response import Response
import pytest
import os
import io

HERE = os.path.dirname(__file__)


@pytest.fixture
def httprequest():
    req = testing.DummyRequest()
    return req


def test_html_views_return_response(httprequest):
    """Home view returns a reponse object."""
    from learning_journal.views.default import (
        list_view,
        detail_view,
        create_view,
        update_view
    )
    assert isinstance(list_view(httprequest), Response)
    assert isinstance(detail_view(httprequest), Response)
    assert isinstance(create_view(httprequest), Response)
    assert isinstance(update_view(httprequest), Response)


def test_list_view_return_proper_content(httprequest):
    """Home view has file content."""
    from learning_journal.views.default import list_view
    file_content = io.open(os.path.join(HERE, 'scripts/index.html')).read()
    response = list_view(httprequest)
    assert file_content == response.text


def test_list_view_is_good():
    """Home view response has file content."""
    from learning_journal.views.default import list_view
    response = list_view(httprequest)
    assert response.status_code == 200


# def test_home_view_raise_exception():
#     """Home view raise exception."""
#     from pyramid_learning_journal.views.default import list_view
#     response =


def test_detail_view_contains_attr():
    """Test that what's returned by view contains journal object."""
    from learning_journal.views.default import detail_view
    request = testing.DummyRequest()
    info = detail_view(request)
    for key in ["category", "creation_date", "id", "description", "amount"]:
        assert key in info.keys()

# @pytest.fixture()
# def testapp():
#     """Create an instance of our app for testing."""
#     from expense_tracker import main
#     app = main({})
#     from webtest import TestApp
#     return TestApp(app)

# def test_layout_root(testapp):
#     """Test that the contents of the root page contains <article>."""
#     response = testapp.get('/', status=200)
#     html = response.html
#     assert 'Created in the Code Fellows 401 Python Program' in html.find("footer").text

# def test_root_contents(testapp):
#     """Test that the contents of the root page contains as many <article> tags as expenses."""
#     from expense_tracker.data.expense_data import EXPENSES
#     response = testapp.get('/', status=200)
#     html = response.html
#     assert len(EXPENSES) == len(html.findAll("article"))


