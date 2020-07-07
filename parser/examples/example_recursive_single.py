

# Вытащить данные из списка объектов с сортировкой
# и переходом по пагинации
# Сортировка осуществляется по объектно

xpath = '//div[@class="quote"]/span[@class="text"]/text()'

down = Asynchronous()

down.domain = 'http://quotes.toscrape.com'
down.start_url = 'http://quotes.toscrape.com/'

# Нет выделенного объекта
# Путь от корня документа
down.xpath_get_data = {
    'author': '//small[@class="author"]/text()',
    'text': '//span[@class="text"]/text()'
}
# ссылка на следующую страницу
down.xpath_next_href = '//li[@class="next"]/a/@href'

# Первый запрос (также устанавливается ссылка на следующую страницу)
res = down.run()

for item in res:
    print(item)


while True:
    # Перезапуск объекта с новыми ссылками
    res = down.run()

    for item in res:
        print(item)

    # После того как закончатся ссылки на следующую вернёт False
    if not bool(down.start_url):
        break


