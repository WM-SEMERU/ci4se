def set_itunes_closed_captioned(self):
    try:
        self.itunes_closed_captioned = self.soup.find(
            'itunes:isclosedcaptioned').string
        self.itunes_closed_captioned = self.itunes_closed_captioned.lower()
    except AttributeError:
        self.itunes_closed_captioned = None