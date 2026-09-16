def logos(self):
    if self._logos is None:
        self._logos = list()
        soup = BeautifulSoup(self.html, 'html.parser')
        info = soup.find('table', {'class': 'infobox'})
        if info is not None:
            children = info.findAll('', {'class': 'image'})
            for child in children:
                self._logos.append('https:' + child.img['src'])
    return self._logos