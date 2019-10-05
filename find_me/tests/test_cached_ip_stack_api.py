from unittest.mock import patch

from find_me.ipstack import CachedIPStackAPI


class Response:
    def __init__(self, text: dict):
        self.text = text


def test_when_ip_is_new_calls_external_service():
    mock = patch('find_me.ipstack.requests.get', return_value=Response("{}"))

    with mock as external_service:
        CachedIPStackAPI().get_location('127.0.0.1')
        CachedIPStackAPI().get_location('127.0.0.2')
        CachedIPStackAPI().get_location('127.0.0.3')

    assert external_service.call_count == 3


def test_when_ip_has_been_seen_before_does_not_call_external_service():
    mock = patch('find_me.ipstack.requests.get', return_value=Response("{}"))
    api = CachedIPStackAPI()

    with mock as external_service:
        api.get_location('127.0.0.1')
        api.get_location('127.0.0.2')
        api.get_location('127.0.0.1')

    assert external_service.call_count == 2


def test_when_cache_reaches_limit_should_clean_itself():
    mock = patch('find_me.ipstack.requests.get', return_value=Response("{}"))
    api = CachedIPStackAPI(max_cache_size=2)

    with mock as external_service:
        api.get_location('127.0.0.1')
        api.get_location('127.0.0.1')
        api.get_location('127.0.0.2')
        api.get_location('127.0.0.2')
        api.get_location('127.0.0.3')
        api.get_location('127.0.0.4')
        api.get_location('127.0.0.1')

    assert external_service.call_count == 5
