import asyncio
import aiohttp
from bs4 import BeautifulSoup
from collections import defaultdict
import time


class Factory:

    def __init__(self):
        self.url = "https://ru.wikipedia.org/w/index.php?title=%D0%9A%D0"\
                    "%B0%D1%82%D0%B5%D0%B3%D0%BE%D1%80%D0%B8%D1%8F:%D0%96"\
                    "%D0%B8%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B5_%D0%BF%D0"\
                    "%BE_%D0%B0%D0%BB%D1%84%D0%B0%D0%B2%D0%B8%D1%82%D1%83"
        self.data = defaultdict(int)
        self.alphabet = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ж', 'З', 'И', 'Й', 'К',
                         'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У', 'Ф', 'Х',
                         'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']

    async def get_urls(self, letter: str):
        url = self.url + '&from=' + letter
        while url:
            url = await self.get_page_content(url, letter)

    async def get_page_content(self, url, letter: str):
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                content = await response.read()
                soup = BeautifulSoup(content, 'lxml')
                links = soup.find('div', attrs={'class': 'mw-category-group'}).find_all('li')
                if letter in ('Ы', 'Ъ', 'Ь'):
                    self.data[letter] = 0
                    return None
                letters = [letter.text[0] for letter in links]
                if letters[0] != letter:
                    return None
                self.data[letter] += len(letters)
                link_url = soup.find('a', string='Следующая страница')
                if not link_url:
                    return None
                url = 'https://ru.wikipedia.org/' + link_url.get('href')
        return url

    async def main(self):
        tasks = [self.get_urls(letter) for letter in self.alphabet]
        await asyncio.gather(*tasks)
        return self.data


if __name__ == "__main__":
    t1 = time.time()
    factory = Factory()
    result = asyncio.run(factory.main())
    test = 1
    for k, v in sorted(result.items()):
        print(k, v)
    print(time.time() - t1)
