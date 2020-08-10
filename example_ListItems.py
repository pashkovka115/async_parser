from schemes.ListItems import ListItems

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

# print(list_parser.get_content())
for page in list_parser.get_content():
    print(page)

