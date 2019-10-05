import json
from dataclasses import dataclass
from typing import Optional

import requests


@dataclass
class Location:
    country: str
    region: str
    city: str
    zipcode: str
    country_flag: str


class LocationTracker:

    def track(self, request) -> Optional[Location]:
        data = IPStackTracker().track(request.remote_addr)
        location = LocationFactory.from_ipstack(data)

        if not location.country:
            return None

        return location


class IPStackTracker:

    def __init__(self, access_key: str = None):
        self._access_key = access_key or 'd7d14990b39e3dd4675f1c95f0d672b1'

    def track(self, ip_address: str) -> dict:
        url = f'http://api.ipstack.com/{ip_address}?access_key={self._access_key}'  # noqa: E501
        response = requests.get(url)
        return json.loads(response.text)


class LocationFactory:

    @staticmethod
    def from_ipstack(data) -> Location:
        return Location(
            country=data['country_name'],
            country_flag=data['location']['country_flag'],
            region=data['region_code'],
            city=data['city'],
            zipcode=data['zip'],
        )
