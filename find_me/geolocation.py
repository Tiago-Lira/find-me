from dataclasses import dataclass
from typing import Optional


@dataclass
class Location:
    country: str
    region: str
    city: str
    zipcode: str
    country_flag: str


class GLocationExternalAPI:

    def get_location(self, ip_address: str) -> Location:
        raise NotImplementedError


class GLocationFinder:

    def __init__(self, api: GLocationExternalAPI):
        self._api = api

    def find(self, ip_address: str) -> Optional[Location]:
        location = self._api.get_location(ip_address)

        if not location.country:
            return None

        return location
