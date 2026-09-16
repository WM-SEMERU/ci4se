def get_description(self):
    if self._description:
        return self._description
    try:
        trailerURL = 'http://trailers.apple.com%s' % self.baseURL
        response = urllib.request.urlopen(trailerURL)
        Reader = codecs.getreader('utf-8')
        responseReader = Reader(response)
        trailerHTML = responseReader.read()
        description = re.search(
            '<meta *name="Description" *content="(.*?)" *[/]*>', trailerHTML)
        if description:
            self._description = description.group(1)
        else:
            self._description = 'None'
    except:
        self._description = 'Error'
    return self._description