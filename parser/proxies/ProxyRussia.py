from parser.utils import Utils
import os
import random
from lxml import html, etree
from parser.headers import HEADERS
from requests_html import HTMLSession



class ProxyRussia(Utils):
    def __init__(self):
        """
        :param resave: файл с проксями обновлять?
        """
        print('Скачиваю', 'ProxyRussia')
        self.filename = 'downloaded_proxies_russia_list.txt'
        self.url = 'http://178.132.2.178/'
        session = HTMLSession()
        r = session.get(self.url, headers=random.choice(HEADERS), timeout=30)
        r.html.render(sleep=1, keep_page=True, scrolldown=1)
        self.html = r.html.xpath("//table[@class='main']/tbody/tr[2]/td/table[3]/tbody/tr/td[@class='content']/table[1]", first=True).html
        # print(self.html)
        self._save_proxies()


    def _save_proxies(self):
        trs = self.xpath(self.html, '//tr')
        # print(trs)
        if os.path.exists(self.filename):
            os.unlink(self.filename)

        with open(self.filename, 'w') as f:
            for tr in trs:
                try:
                    h_tr = etree.tostring(tr).decode("utf-8")
                    # print('===', self.xpath(h_tr, '//td[1]/text()')[0]) # isdigit
                    if str(self.xpath(h_tr, '//td[1]/text()')[0]).isdigit():
                        item = {
                            'ip': self.xpath(h_tr, '//td[2]/text()')[0],
                            'port': self.xpath(h_tr, '//td[3]/text()')[0],
                            'protocol': self.xpath(h_tr, '//td[4]/text()')[0],
                            'type': self.xpath(h_tr, '//td[5]/text()')[0],
                        }

                        if item['protocol'] == 'HTTP':
                            f.write(item['ip'] + ':' + item['port'] + '\n')
                except:
                    pass


    def get_proxies(self) -> list:
        if os.path.exists(self.filename):
            data = []
            with open(self.filename, 'r') as f:
                for line in f.readlines():
                    data.append(line.strip())
            return data
        return []




































