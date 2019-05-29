from django_webtest import WebTest
import pytest

from .. import factories

pytestmark = pytest.mark.django_db

def test_can_create_an_empty_poll(django_app):
    resp = django_app.get('/')
    form = resp.form
    form['name'] = 'Max'
    response = form.submit().follow()
    print(response)

def test_can_get_poll_share_url(django_app):
    poll = factories.PollFactory()
    resp = django_app.get(poll.get_share_url())
