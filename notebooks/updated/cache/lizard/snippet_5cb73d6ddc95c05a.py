def _load(self, titles=[], descriptions=[], images=[], urls=[], **kwargs):
    enough = lambda items: items
    if config.GET_ALL_DATA or not enough(self.titles):
        titles = filter(None, map(self._clean_text, titles))
        self.titles.extend(titles)
    if config.GET_ALL_DATA or not enough(self.descriptions):
        descriptions = filter(None, map(self._clean_text, descriptions))
        self.descriptions.extend(descriptions)
    if config.GET_ALL_DATA:
        images = filter(None, map(self._filter_image, images))
        self.images.extend(images)
    elif not enough(self.images):
        for i in images:
            image = self._filter_image(i)
            if image:
                self.images.append(image)
            if enough(self.images):
                break