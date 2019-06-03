from django_webtest import WebTest
import pytest
from .. import factories, models

pytestmark = pytest.mark.django_db

def test_can_create_a_poll_and_see_share_url(django_app):
    factories.QuestionFactory()
    factories.QuestionFactory()
    factories.QuestionFactory()

    assert models.Poll.objects.count() == 0
    response = django_app.get('/')
    form = response.form

    form['name'] = 'Max'
    form['answers-0-value'] = 'Y'
    form['answers-1-value'] = 'Y'
    form['answers-2-value'] = 'Y'
    response = form.submit()
    response.follow()
    assert models.Poll.objects.count() == 1
    assert models.Answer.objects.count() == 3

def test_cant_create_a_poll_wo_answering_all_questions(django_app):
    assert models.Poll.objects.count() == 0
    resp = django_app.get('/')
    form = resp.form

    form['name'] = 'Max'
    form['answers-0-value'] = 'Y'
    response = form.submit()

def test_can_compate_a_poll_0(django_app):
    questions = [
        factories.QuestionFactory(),
        factories.QuestionFactory(),
        factories.QuestionFactory(),
    ]
    assert models.Poll.objects.count() == 0
    poll = factories.PollFactory(name='Johannes')

    factories.AnswerFactory(value='Y', poll=poll, question=questions[0])
    factories.AnswerFactory(value='Y', poll=poll, question=questions[1])
    factories.AnswerFactory(value='Y', poll=poll, question=questions[2])

    response = django_app.get(poll.get_participate_url())
    assert response.status_code == 200
    assert poll.get_participate_url() == '/polls/1/participate'

    form = response.form
    form['name'] = 'Vova'
    form['answers-0-value'] = 'N'
    form['answers-1-value'] = 'N'
    form['answers-2-value'] = 'N'
    response = form.submit()
    assert response.status_code == 302
    assert response.url == '/polls/2/compare'
    response = response.follow()
    assert models.Poll.objects.count() == 2
    assert response.text == 'Vova and Johannes answers` are 0% equal\n'

def test_can_compare_a_poll_100(django_app):
    questions = [
        factories.QuestionFactory(),
        factories.QuestionFactory(),
        factories.QuestionFactory(),
    ]
    assert models.Poll.objects.count() == 0
    poll = factories.PollFactory(name='Johannes')

    factories.AnswerFactory(value='Y', poll=poll, question=questions[0])
    factories.AnswerFactory(value='Y', poll=poll, question=questions[1])
    factories.AnswerFactory(value='Y', poll=poll, question=questions[2])

    response = django_app.get(poll.get_participate_url())
    assert response.status_code == 200
    assert poll.get_participate_url() == '/polls/1/participate'

    form = response.form
    form['name'] = 'Vova'
    form['answers-0-value'] = 'Y'
    form['answers-1-value'] = 'Y'
    form['answers-2-value'] = 'Y'
    response = form.submit()
    response.showbrowser()
    assert response.status_code == 302
    assert response.url == '/polls/2/compare'
    response = response.follow()
    assert models.Poll.objects.count() == 2
    assert models.Answer.objects.count() == 6
    assert response.text == 'Vova and Johannes answers` are 100% equal\n'

def test_can_compare_a_poll_66(django_app):
    questions = [
        factories.QuestionFactory(),
        factories.QuestionFactory(),
        factories.QuestionFactory(),
    ]
    assert models.Poll.objects.count() == 0
    poll = factories.PollFactory(name='Johannes')

    factories.AnswerFactory(value='Y', poll=poll, question=questions[0])
    factories.AnswerFactory(value='Y', poll=poll, question=questions[1])
    factories.AnswerFactory(value='N', poll=poll, question=questions[2])

    response = django_app.get(poll.get_participate_url())
    assert response.status_code == 200
    assert poll.get_participate_url() == '/polls/1/participate'

    form = response.form
    form['name'] = 'Vova'
    form['answers-0-value'] = 'Y'
    form['answers-1-value'] = 'Y'
    form['answers-2-value'] = 'Y'
    response = form.submit()
    response.showbrowser()
    assert response.status_code == 302
    assert response.url == '/polls/2/compare'
    response = response.follow()
    assert models.Poll.objects.count() == 2
    assert models.Answer.objects.count() == 6
    assert response.text == 'Vova and Johannes answers` are 66% equal\n'
