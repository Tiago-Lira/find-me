import json

import requests

from find_me.geolocation import GLocationExternalAPI, Location


class IPStackAPI(GLocationExternalAPI):

    def __init__(self, access_key: str = None):
        self._access_key = access_key or 'd7d14990b39e3dd4675f1c95f0d672b1'

    def get_location(self, ip_address: str) -> Location:
        url = f'http://api.ipstack.com/{ip_address}?access_key={self._access_key}'  # noqa: E501
        response = requests.get(url)
        data = json.loads(response.text)
        return Location(
            country=data.get('country_name'),
            country_flag=data.get('location', {}).get('country_flag'),
            region=data.get('region_code'),
            city=data.get('city'),
            zipcode=data.get('zip'),
        )


class CachedIPStackAPI(IPStackAPI):

    def __init__(self, *args, **kwargs):
        self.__cache = {}
        self.__max_size = kwargs.pop('max_cache_size', 10000)
        super().__init__(*args, **kwargs)

    def get_location(self, ip_address: str) -> dict:
        result = self.__cache.get(ip_address)

        if not result:
            result = super().get_location(ip_address)
            self._clear_cache_if_needed()
            self.__cache[ip_address] = result

        return result

    def _clear_cache_if_needed(self):
        if len(self.__cache) >= self.__max_size:
            self.__cache = {}
