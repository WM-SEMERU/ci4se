def sign(self, xml_doc):
    try:
        self.client = Client(self.url)
    except ValueError as e:
        self.message = e.message
    except URLError:
        self.message = ('The url you provided: ' + 
            '%s could not be reached' % self.url)