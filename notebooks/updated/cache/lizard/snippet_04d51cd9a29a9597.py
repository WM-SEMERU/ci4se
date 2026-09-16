def set_author(self, *, name, url=EmptyEmbed, icon_url=EmptyEmbed):
    self._author = {'name': str(name)}
    if url is not EmptyEmbed:
        self._author['url'] = str(url)
    if icon_url is not EmptyEmbed:
        self._author['icon_url'] = str(icon_url)
    return self