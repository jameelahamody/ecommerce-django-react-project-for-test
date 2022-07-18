import pytest
from django.contrib.auth import authenticate, get_user_model
from django.http import HttpRequest
from selenium.webdriver.firefox import webdriver
from rest_framework.test import APIClient
from django.contrib.auth.models import User

@pytest.fixture()
def user_1(db):
    return User.objects.create_user("test-user")

@pytest.mark.django_db
def test_get_user_by_username():
    user1=User.objects.create_user('test','test@test.com','test')
    get_user=User.objects.get(username=user1.username)
    assert get_user.username == user1.username

@pytest.mark.django_db
def test_get_user_by_email():
    user1=User.objects.create_user('test','test@test.com','test')
    get_user=User.objects.get(email=user1.email)
    assert get_user.username == user1.email

# to check whether user is available or not?
        # the password verified for the user
@pytest.mark.django_db
def test_authenticate_user():
    user = authenticate(username='test1',password='test1')
    if user is not None:
        if user.is_active:

            print("User is valid, active and authenticated")
        else:
            print("The password is valid, but the account has been disabled!")
    else:
        # the authentication system was unable to verify the username and password
        print("The username and password were incorrect.")
# @pytest.mark.django_db
# def test_is_trusted_request():
#      user = User(username='test_user', is_active=True, is_staff=True)
#      request = HttpRequest()
#      request.user = user
#      request.META['REMOTE_ADDR'] = '127.0.0.1'
#      context = {'request': request}
#      assert  request(context) is True
#      user.is_active = False
#      assert request.context is False
#      user.is_active = True
#      user.is_staff = False
#      assert request.context is False
#      request.META['REMOTE_ADDR'] = '1.2.3.4'
#      assert request.context is False
@pytest.mark.django_db
def test_user_is_active_after_creation():
   User=get_user_model()
   user = User.objects.create_user(username='normal',email='normaluser@user.com', password='hii')
   assert user.is_active is True
@pytest.mark.django_db
def test_create_superuser():
   User=get_user_model()
   superuser = User.objects.create_superuser(username='superl',email='superuser@user.com', password='Imsuper')
   assert superuser.is_active is True
@pytest.mark.django_db
def test_delete_user(user_1):
    user = User.objects.get(id=user_1.id)
    user.delete()
    count = User.objects.all().count()
    assert count == 0