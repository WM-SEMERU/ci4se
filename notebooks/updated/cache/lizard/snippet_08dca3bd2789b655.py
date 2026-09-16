def comicPageLink(self, comic, url, prevUrl):
    for handler in _handlers:
        handler.comicPageLink(comic, url, prevUrl)