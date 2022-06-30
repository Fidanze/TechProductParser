from abc import ABC, abstractmethod

import urllib3
from lxml import html


class RequestBased(ABC):
    cities = {}

    def __init__(self, url):
        self.httpClient = urllib3.PoolManager()
        self.html = html
        self.__class__.cities = self.__class__.getCities()
        assert self.__class__.cities, 'Parser dont have cities'
        self.url = url

    @classmethod
    @abstractmethod
    def getCities(cls) -> dict[str, str]:
        pass

    def setCurrentCity(self, city: str) -> None:
        self.currentCity = city

    @abstractmethod
    def parseOptions(self):
        pass

    @abstractmethod
    def parseAvailability(self):
        pass

    @abstractmethod
    def getAvailability(self):
        pass

    @abstractmethod
    def getProductOptions(self):
        pass
