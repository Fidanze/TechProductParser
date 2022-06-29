from abc import ABC, abstractmethod
import urllib3

class RequestBased(ABC):
    def __init__(self):
        self.cities = self.getCities()
        self.http = urllib3.PoolManager()

    @abstractmethod
    def getCities(self):
        pass

    @abstractmethod
    def setCurrentCity(self, city: str) -> None:
        self.currentCity = city

    @abstractmethod
    def parseOptions(self):
        pass

    @abstractmethod
    def parseAvailability(self):
        pass

    @abstractmethod
    def __getAvailability(self):
        pass

    @abstractmethod
    def __getProductOptions(self):
        pass
