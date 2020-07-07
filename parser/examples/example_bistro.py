


down = Asynchronous()

down.domain = 'http://quotes.toscrape.com'
down.start_url = 'http://quotes.toscrape.com/'

down.block_xpath = '//div[@class="quote"]'
down.xpath_get_data = {
    'author': '//small[@class="author"]/text()',
    'text': '//span[@class="text"]/text()'
}
down.xpath_next_href = '//li[@class="next"]/a/@href'

down.set_urls([
    ('http://quotes.toscrape.com/', ),
    ('http://quotes.toscrape.com/page/2/', {'ключ': 'здесь тоже может быть xpath, но не обязательно или вместо self.xpath_get_data'}),
    ('http://quotes.toscrape.com/page/3/', ),
])


async def task1():
    return 'Task1'

async def task2(param):
    return f'Task2 - {param}'

# Добавить задачи. Будут выполнятся асинхронно с другими задачами
down.add_task(task1)
down.add_task(task2, param='value')

# Запуск программы происходит здесь! До этого только настройки программы.
res = down.run()


print(down.start_url)
for item in res:
    print(item)


