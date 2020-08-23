from parsera import Parser
from parsera.HTTPQuery import HTTPQuery


class Base:
    def __init__(self, domain: str, start_url: str = None, elements_xpath: dict = None,
                 semaphore: int = 10, sleeping=(2, 5), blocks_xpath: str = None,
                 xpath_to_singles_links=None,
                 xpath_next_url=None, timeout=30, proxy=None):
        self._domain = domain
        self._http_query = HTTPQuery(domain, start_url, semaphore, sleeping, timeout, proxy)
        self._start_url = start_url
        self._blocks_xpath = blocks_xpath
        self.parser = Parser(
            domain=domain, blocks_xpath=blocks_xpath,
            elements_xpath=elements_xpath,
            xpath_to_singles_links=xpath_to_singles_links,
            # xpath_single_elements=xpath_single_elements,
            xpath_next_url=xpath_next_url,
        )
        self.text_response = None