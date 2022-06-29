from abc import ABC, abstractmethod


class SeleniumBased(ABC):
    @abstractmethod
    def parseOptions(self):
        pass
    @abstractmethod
    def parseAvailability(self):
        pass

    @abstractmethod
    def __getPageNumber(self):
        pass
    @abstractmethod
    def __getPages(self):
        pass
    @abstractmethod
    def __getProductOptions(self):
        pass
    @abstractmethod
    def __getAvailability(self):
        pass



