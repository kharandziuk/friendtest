from django_webtest import WebTest
import pytest

pytestmark = pytest.mark.django_db

def test_can_create_an_empty_poll(django_app):
    resp = django_app.get('/')
    form = resp.form
    form['name'] = 'Max'
    response = form.submit().follow()
    print(response)
