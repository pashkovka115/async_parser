from parsera import Parser

parser = Parser(
        domain='http://quotes.toscrape.com',
        blocks_xpath='//div[@class="quote"]',
        elements_xpath={
            'text': '//span[@class="text"]//text()',
            'author': '//small[@class="author"]//text()',
            'link': '//span/a/@href'
        },
        xpath_to_singles_links='//span/a/@href',
        xpath_next_url='//li[@class="next"]/a/@href',
)

html = parser.file_get_contents('test_list_page.html') # or http response.text
parsed_elements = parser.parse_html(html)

print(parsed_elements)


