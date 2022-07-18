import pytest
from http.client import InvalidURL
from pyhttptest import utils

def test_prepare_url():
    host = 'http://localhost:8000/'
    endpoint = 'users'
    url = utils.prepare_url(host, endpoint)

    assert url == 'http://localhost:8000/users'
def test_prepare_url_with_none_type_arg():
    url = utils.prepare_url('http://localhost:8000/', None)

    assert url is None


def test_prepare_url_with_host_arg_ends_with_backslash():
    host = 'http://localhost:8000/'
    endpoint = 'users'
    url = utils.prepare_url(host, endpoint)

    assert url == 'http://localhost:8000/users'


def test_prepare_url_with_endpoint_arg_starts_with_backslash():
    host = 'http://localhost:8000/'
    endpoint = '/users'
    url = utils.prepare_url(host, endpoint)

    assert url == 'http://localhost:8000/users'


def test_prepare_url_with_both_host_and_endpoint_args_contains_backslash():
    host = 'http://localhost:8000/'
    endpoint = '/users'
    url = utils.prepare_url(host, endpoint)

    assert url == 'http://localhost:8000/users'


def test_prepare_url_with_invalid_host_arg_format():
    with pytest.raises(InvalidURL) as exc:
        host = 'localhost.com'
        endpoint = 'users'
        utils.prepare_url(host, endpoint)

    assert 'Invalid URL' in str(exc.value)


def test_prepare_url_with_not_supported_url_scheme():
    with pytest.raises(InvalidURL) as exc:
        host = 'ftp://localhost.com'
        endpoint = 'users'
        utils.prepare_url(host, endpoint)

    assert 'Invalid URL scheme' in str(exc.value)