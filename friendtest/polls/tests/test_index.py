from django_webtest import WebTest

def test_1(django_app):
    resp = django_app.get('/')
    print(resp)
