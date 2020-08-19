from random import randint
from time import sleep

from schemes.ListItems import ListItems
from schemes.SingleItem import SingleItem



list_parser = ListItems(
        domain='http://quotes.toscrape.com',
        start_url='http://quotes.toscrape.com',
        blocks_xpath='//div[@class="quote"]',
        elements_xpath={
            'text': '//span[@class="text"]//text()',
            'author': '//small[@class="author"]//text()',
            'link': '//span/a/@href'
        },
        xpath_to_singles_links='//span/a/@href',
        xpath_next_url='//li[@class="next"]/a/@href',
)

for page in list_parser.get_content():
    single = SingleItem(
            domain='http://quotes.toscrape.com',
            elements_xpath={
                'author': "//h3[@class='author-title']/text()",
                'birthday': '//p/span[@class="author-born-date"]/text()',
                'biography': '//div[@class="author-description"]/text()'
            },
    )
    single.add_urls(page['singles_links'])

    for single_page in single.get_content():
        print(single_page)

    sleep(randint(2, 5))
