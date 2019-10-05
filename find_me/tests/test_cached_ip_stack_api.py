from unittest.mock import patch

from find_me.ipstack import CachedIPStackAPI


class Response:
    def __init__(self, text: dict):
        self.text = text


def test_when_ip_is_new_calls_external_service():
    mock = patch('find_me.ipstack.requests.get', return_value=Response("{}"))

    with mock as external_service:
        CachedIPStackAPI().get_location('127.0.0.1')

    external_service.assert_called_once()


def test_when_ip_has_been_seen_before_does_not_call_external_service():
    mock = patch('find_me.ipstack.requests.get', return_value=Response("{}"))
    api = CachedIPStackAPI()

    with mock as external_service:
        api.get_location('127.0.0.1')
        api.get_location('127.0.0.1')
        api.get_location('127.0.0.1')

    external_service.assert_called_once()
