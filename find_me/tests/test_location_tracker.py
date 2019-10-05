from unittest.mock import patch

from find_me.location import Location, LocationTracker


class Response:
    def __init__(self, text: dict):
        self.text = text


def test_returns_location_instance():
    response = Response("""
    {
        "ip": "66.171.191.134",
        "type": "ipv4",
        "continent_code": "NA",
        "continent_name": "North America",
        "country_code": "US",
        "country_name": "United States",
        "region_code": "WA",
        "region_name": "Washington",
        "city": "Seattle",
        "zip": "98121",
        "latitude": 47.61347961425781,
        "longitude": -122.34738159179688,
        "location": {
            "geoname_id": 5809844,
            "capital": "Washington D.C.",
            "languages": [{
                "code": "en",
                "name": "English",
                "native": "English"
            }],
            "country_flag": "http://assets.ipstack.com/flags/us.svg",
            "country_flag_emoji": "\ud83c\uddfa\ud83c\uddf8",
            "country_flag_emoji_unicode": "U+1F1FA U+1F1F8",
            "calling_code": "1",
            "is_eu": false
        }
    }
    """)

    with patch('find_me.location.requests.get', return_value=response):
        result = LocationTracker().track('127.0.0.1')

    assert isinstance(result, Location)


def test_when_location_is_not_found_returns_none():
    response = Response("""
    {
        "ip": null,
        "type": null,
        "continent_code": null,
        "continent_name": null,
        "country_code": null,
        "country_name": null,
        "region_code": null,
        "region_name": null,
        "city": null,
        "zip": null,
        "latitude": null,
        "longitude": null,
        "location": {
            "geoname_id": null,
            "capital": null,
            "languages": [],
            "country_flag": null,
            "country_flag_emoji": null,
            "country_flag_emoji_unicode": null,
            "calling_code": null,
            "is_eu": false
        }
    }
    """)

    with patch('find_me.location.requests.get', return_value=response):
        result = LocationTracker().track('127.0.0.1')

    assert result is None
