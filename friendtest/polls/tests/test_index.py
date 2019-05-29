from django_webtest import WebTest

def test_can_create_an_empty_poll(django_app):
    resp = django_app.get('/')
    form = resp.form
    print(resp)
