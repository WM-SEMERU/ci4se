def link_empty_favicon_fallback(self):
    self.favicon_fallback = os.path.join(os.path.dirname(__file__),
        'favicon.ico')