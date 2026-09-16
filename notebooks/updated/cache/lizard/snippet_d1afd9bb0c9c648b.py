def get_by_enclosures(self, enclosure_urls):
    enclosure_urls = map(str.strip, enclosure_urls)
    enclosure_urls = filter(None, enclosure_urls)
    return BitloveResponse(self.opener, enclosure_urls)