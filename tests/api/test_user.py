import pytest
import requests
from django.contrib.auth.models import User
from django.utils import timezone
from rest_framework.test import APIClient
import requests
import json

from base.models import Product
# TOKEN=None
# USER_ID = None
'''
Unit tests -> checking user creation func
'''
@pytest.mark.django_db
def test_user_create():
    User.objects.create_user('test','test@test.com','test')
    count = User.objects.all().count()
    assert count == 1

@pytest.fixture()
def user_1(db):
    return User.objects.create_user("test-user")

@pytest.mark.django_db
def test_set_check_password(user_1):
    user_1.set_password("new-password")
    assert user_1.check_password("new-password") is True



'''
Integration testing testing api to register user
'''
@pytest.mark.django_db
def test_register_user():
    client = APIClient()

    payload = dict(
        name="testing123",
        email="test11@test.com",
        password="super-secret"
    )

    response = client.post("/api/users/register/", payload)

    data = response.data

    assert data["name"] == payload["name"]
# def test_created_user_can_be_deleted():
#     client = APIClient()
#
#
#     response = client.delete_person(user_1)
#     assert(response.status_code).is_equal_to(requests.codes.ok)



# @pytest.fixture()
# def check_ability_gen_token():
#     """check is is possible to generate token.
#     If user not exists then
#     status = failed
#     result = User authorization failed.
#     """
#     response = requests.post(f'{TARGET_API}{ACCOUNT}GenerateToken')
#     body = response.json()
#     return True if body["status"] == "Success" else False
# @pytest.fixture()
# def user_1(db):
#     return User.objects.create_user("test-user")

# def test_delete_user():
#     TARGET_API = "http://127.0.0.1:8000/"
#     ACCOUNT = 'hamodyjameela@gmail.com'
#     PAYLOAD = json.dumps({"username": "hamodyjameela@gmail.com", "password": "jameela58@"})
#     HEADERS = {'Content-Type': 'application/json'}
#     USER_NAME = (json.loads(PAYLOAD))["username"]
#     headers_auth = {'Content-Type': 'application/json',
#                         'Authorization': f'Bearer {TOKEN}'}
#     response = requests.delete(f'{TARGET_API}{ACCOUNT}User/{USER_ID}', headers=headers_auth)
#     status_code = response.status_code
#
#    #HTTP_NO_CONTENT = 204
#     if status_code == 204:
#          assert 1==1
#      # elif status_code == HTTP_OK:
#      #     assert check_ability_gen_token(),
#      #                     f'User not deleted! Status code{status_code}, but operation could not complete!')
#     else:
#          assert 5==1
#                          # f'Unexpected Error on user deletion, status code: "{status_code}"!')


