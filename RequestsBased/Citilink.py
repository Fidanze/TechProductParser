import json
import math

from bs4 import BeautifulSoup
from urllib3 import *

from base import RequestBased


class CitilinkParser(RequestBased):
    base_url: str = 'https://www.citilink.ru/'

    @classmethod
    def getCities(cls) -> dict[str, str]:
        response: HTTPResponse = PoolManager().request(method='GET',
                                                                         url=cls.base_url + 'cities/content/')
        assert response.status == 200, f'Request failed with status {response.status}'
        soup: BeautifulSoup = BeautifulSoup(json.loads(response.data)['html'].replace('\n', '').strip(), 'lxml')
        cities_html = soup.findAll('a', {'class': 'CitiesSearch__item-city'})
        return {city.attrs['data-search'].capitalize(): city.attrs['href'].split('=')[-1][::-1] for city in
                cities_html}

    def getPageNumber(self) -> int:
        response: HTTPResponse = self.httpClient.request(method='GET', url=self.url, fields={
            'action': 'ChangeCity',
            'space': self.__class__.cities[self.currentCity]
        })
        assert response.status == 200, f'Request failed with status {response.status}'
        soup: BeautifulSoup = BeautifulSoup(response.data.decode('UTF-8'), 'lxml')
        number_text = soup.find('div', {'class': 'Subcategory__count'}).text
        return math.ceil(int(number_text.split()[0]) / 49)

    def getPages(self) -> list[str]:
        return [self.url + f'?p={i + 1}' for i in range(self.getPageNumber())]

    def getProductOptions(self):
        pass

    def getAvailability(self):
        pass

    def parseOptions(self):
        pages = self.getPages()

    def parseAvailability(self):
        pages = self.getPages()

        for page in pages:
            response: HTTPResponse = self.httpClient.request(method='GET', url=page, fields={
                'action': 'ChangeCity',
                'space': self.currentCity
            })
            assert response.status == 200, f'Request failed with status {response.status}'
            soup: BeautifulSoup = BeautifulSoup(response.data.decode("utf-8"), 'lxml')
            products = soup.select('div.ProductCardHorizontal.js--ProductCardInListing')
            for product in products:
                name = json.loads(product.attrs['data-params'])['shortName']
                price = product.attrs['data-price']
                isavailable = not ('ProductCardHorizontal__block_not-available' in
                                   product.find('div', {'class': 'ProductCardHorizontal__header-block'}).attrs['class'])
                print(isavailable)


if __name__ == '__main__':
    url = 'https://www.citilink.ru/catalog/videokarty/'
    parser = CitilinkParser(url)
    parser.setCurrentCity('Уфа')
    parser.parseAvailability()
    print('the end.')
