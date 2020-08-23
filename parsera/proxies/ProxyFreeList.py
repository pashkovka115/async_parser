import os
import random
from lxml import html, etree
from parsera.utils import Utils
from parsera.headers import HEADERS
from requests_html import HTMLSession


# , headers=random.choice(HEADERS), timeout=30

class ProxyFreeList(Utils):
    def __init__(self, resave:bool):
        """
        :param resave: файл с проксями обновлять?
        """
        print('Скачиваю', 'ProxyFreeList')
        self.resave = resave
        self.filename = 'downloaded_proxies_free_list.txt'
        self.url = 'https://free-proxy-list.net/'
        session = HTMLSession()
        r = session.get(self.url, headers=random.choice(HEADERS), timeout=30)
        r.html.render(sleep=1, keep_page=True, scrolldown=1)
        self.html = r.html.xpath('//table[@id="proxylisttable"]', first=True).html
        self._save_proxies()


    def _save_proxies(self):
        trs = self.xpath(self.html, '//tbody/tr')
        if self.resave and os.path.exists(self.filename):
            os.unlink(self.filename)
        elif os.path.exists(self.filename):
            return


        with open(self.filename, 'w') as f:
            for tr in trs:
                try:
                    h_tr = etree.tostring(tr).decode("utf-8")

                    item = {
                        'ip': self.xpath(h_tr, '//td[1]/text()')[0],
                        'port': self.xpath(h_tr, '//td[2]/text()')[0],
                        'code': self.xpath(h_tr, '//td[3]/text()')[0],
                        'country': self.xpath(h_tr, '//td[4]/text()')[0],
                        'anonymity': self.xpath(h_tr, '//td[5]/text()')[0],
                        'google': self.xpath(h_tr, '//td[6]/text()')[0],
                        'https': self.xpath(h_tr, '//td[7]/text()')[0],
                        'last_checked': self.xpath(h_tr, '//td[8]/text()')[0]
                    }
                    if item['https'] == 'no':
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























