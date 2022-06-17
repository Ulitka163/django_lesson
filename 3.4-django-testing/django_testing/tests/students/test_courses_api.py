import pytest

from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def courses_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_course_retrieve(client, courses_factory):
    courses = courses_factory(_quantity=10)
    course_id = courses[2].pk

    response = client.get(f'/api/v1/courses/{course_id}/')
    assert response.status_code == 200
    data = response.json()
    assert data['id'] == course_id


@pytest.mark.django_db
def test_courses_list(client, courses_factory):
    courses = courses_factory(_quantity=10)

    response = client.get('/api/v1/courses/')
    assert response.status_code == 200
    data = response.json()
    assert len(data) == len(courses)
    for i, c in enumerate(data):
        assert c['name'] == courses[i].name


@pytest.mark.django_db
def test_course_create(client):
    count = Course.objects.count()

    response = client.post('/api/v1/courses/', data={'name': 'Test'})

    assert response.status_code == 201
    assert Course.objects.count() == count + 1


@pytest.mark.django_db
def test_course_update(client, courses_factory):
    courses = courses_factory(_quantity=10)
    course_id = courses[2].pk

    response = client.patch(f'/api/v1/courses/{course_id}/', data={"name": "Test"}, content_type='application/json')
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == 'Test'


@pytest.mark.django_db
def test_course_delete(client, courses_factory):
    courses = courses_factory(_quantity=10)
    course_id = courses[2].pk

    response = client.delete(f'/api/v1/courses/{course_id}/')
    assert response.status_code == 204
    response_get = client.get('/api/v1/courses/')
    data = response_get.json()
    assert len(data) == len(courses)-1
    for d in data:
        assert d['id'] != course_id


@pytest.mark.django_db
def test_course_filter_id(client, courses_factory):
    courses = courses_factory(_quantity=10)
    course_id = courses[5].pk

    response = client.get(f'/api/v1/courses/?id={course_id}')
    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == course_id


@pytest.mark.django_db
def test_course_filter_name(client, courses_factory):
    courses = courses_factory(_quantity=10)
    course_name = courses[5].name

    response = client.get(f'/api/v1/courses/?name={course_name}')
    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == course_name
