def write_url(self, url, filename, directory=None):
    return self.write_contents(filename, read(url), directory=directory)