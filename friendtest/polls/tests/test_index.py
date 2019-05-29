from django_webtest import WebTest
import pytest

from .. import factories, models

pytestmark = pytest.mark.django_db

def test_can_create_an_empty_poll_and_see_share_url(django_app):
    assert models.Poll.objects.count() == 0
    resp = django_app.get('/')
    form = resp.form
    form['name'] = 'Max'
    response = form.submit().follow()
    assert models.Poll.objects.count() == 1
    print(response)

def test_can_get_poll_share_url(django_app):
    assert models.Poll.objects.count() == 0
    poll = factories.PollFactory(name='Johannes')
    response = django_app.get(poll.get_participate_url())
    assert response.status_code == 200
    assert poll.get_participate_url() == '/polls/1/participate'

    form = response.form
    form['name'] = 'Vova'
    response = form.submit()
    assert response.status_code == 302
    assert response.url == '/polls/2/compare'
    response = response.follow()
    assert models.Poll.objects.count() == 2
    assert response.text == 'Vova and Johannes answers` are 100% equal\n'
