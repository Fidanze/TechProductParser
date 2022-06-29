from urllib3 import *
from base import RequestBased


class CitilinkParser(RequestBased):
    url = 'https://www.citilink.ru/catalog/videokarty/'

    def getCities(self):
        response:HTTPResponse = self.http.request(method='GET', url=self.__class__.url)

        assert response.status == 200, f'Request failed with status {response.status}'


    def parseOptions(self):
        pass

    def parseAvailability(self):
        pass

    def __getPageNumber(self):
        pass

    def __getPages(self):
        page = self.http.request(method='GET', url=self.__class__.url, fields={
            'action': 'ChangeCity',
            'space': self.currentCity
        })

    def __getProductOptions(self):
        pass

    def __getAvailability(self):
        pass
