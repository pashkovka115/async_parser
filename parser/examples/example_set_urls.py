

xpath = '//div[@class="quote"]/span[@class="text"]/text()'

down = Asynchronous()

down.set_urls([
    ('http://quotes.toscrape.com/', xpath),
    ('http://quotes.toscrape.com/page/2/', xpath),
    ('http://quotes.toscrape.com/page/3/', xpath),
])


res = down.run()

for item in res:
    print(item)

print(down.start_url)

