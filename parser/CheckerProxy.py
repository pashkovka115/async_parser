import random
from time import time

import requests
from .headers import HEADERS




class CheckerProxy:

    def __init__(self, judges=None):
        # self.judges = [ todo: в будущем проверку сделаю более жесткую
        #     'http://httpbin.org/get?show_env',
        #     'https://httpbin.org/get?show_env',
        #     # 'smtp://smtp.gmail.com',
        #     # 'smtp://aspmx.l.google.com',
        #     # 'http://azenv.net/',
        #     # 'https://www.proxy-listen.de/azenv.php',
        #     # 'http://www.proxyfire.net/fastenv',
        #     # 'http://proxyjudge.us/azenv.php',
        #     # 'http://ip.spys.ru/',
        #     # 'http://www.proxy-listen.de/azenv.php',
        # ]
        self.original_ip = self._get_ip()
        self.proxies_for_check = []



    def _get_ip(self, proxy=None, chema_serv='https', chema_proxy='http'):
        url = f'{chema_serv}://check-host.net/ip'
        try:
            if bool(proxy):
                r = requests.get(
                    url,
                    proxies={chema_proxy: proxy},
                    headers=random.choice(HEADERS),
                    timeout=10
                )
            else:
                r = requests.get(url)
            if r.status_code == 200:
                return str(r.text).strip()
        except Exception as e:
            pass
            # print('CheckerProxy->_get_ip:', e)



    def get_checked_proxies(self, chema_serv='http', chema_proxy='http'):
        if not hasattr(self.proxies_for_check, '__iter__'):
            raise Exception('Атрибут proxies_for_check должен быть последовательностью')

        good_proxies = []
        print('Пожалуйста подождите, идёт проверка прокси адресов...')
        print(f'Оригинальный ip - {self.original_ip}')
        for proxy in self.proxies_for_check:
            t1 = time()
            ip = self._get_ip(f'{chema_proxy}://{proxy}', chema_serv)
            print(round(time() - t1, 2), 'Проверил', f'{chema_proxy}://{proxy}', f'Изменённый ip: {ip}')
            if ip is not None and self.original_ip != ip:
                good_proxies.append(f'{chema_proxy}://{proxy}')
        return good_proxies


    def save_and_return_proxies(self, file, chema_serv='http', chema_proxy='http'):
        proxies = self.get_checked_proxies(chema_serv, chema_proxy)
        with open(file, 'w') as f:
            for proxy in proxies:
                f.write(str(proxy) + '\n')
        return proxies








