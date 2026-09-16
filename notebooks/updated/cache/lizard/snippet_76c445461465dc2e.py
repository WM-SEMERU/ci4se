def upload(self, fp):
    url = utils.urljoin(self.url, 'pictures')
    response = self.session.post(url, data=fp.read())
    image_urls = response.data
    return image_urls