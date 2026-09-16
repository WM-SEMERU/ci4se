def set_language(self):
    try:
        self.language = self.soup.find('language').string
    except AttributeError:
        self.language = None