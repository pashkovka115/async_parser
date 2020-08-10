from schemes.SingleItem import SingleItem


single = SingleItem(
        domain='http://quotes.toscrape.com',
        # start_url='', - Здесь не нужен
        # blocks_xpath='', - Здесь не нужен
        elements_xpath={
            'author': "//h3[@class='author-title']/text()",
            'birthday': '//p/span[@class="author-born-date"]/text()',
            'biography': '//div[@class="author-description"]/text()'
        },
        # можно задать как дополнительную выборку, будет другая сортировка (необязательно)
        # xpath_to_singles_links='',
        # xpath_next_url='',
)

# необходимо задать адреса страниц. ОБЯЗАТЕЛЬНО!!!
single.add_urls([
    'http://quotes.toscrape.com/author/Albert-Einstein/',
    'http://quotes.toscrape.com/author/J-K-Rowling',
    'http://quotes.toscrape.com/author/Jane-Austen'
])

# print(single.get_content())
for page in single.get_content():
    print(page)




