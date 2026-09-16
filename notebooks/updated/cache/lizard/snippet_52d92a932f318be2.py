def get_scrapy_options(self):
    if self.__scrapy_options is None:
        self.__scrapy_options = {}
        options = self.section('Scrapy')
        for key, value in options.items():
            self.__scrapy_options[key.upper()] = value
    return self.__scrapy_options