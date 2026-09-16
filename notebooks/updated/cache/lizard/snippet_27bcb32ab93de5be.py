def load(self, carddict):
    self.code = carddict['code']
    if isinstance(self.code, text_type):
        self.code = eval(self.code)
    self.name = carddict['name']
    self.abilities = carddict['abilities']
    if isinstance(self.abilities, text_type):
        self.abilities = eval(self.abilities)
    self.attributes = carddict['attributes']
    if isinstance(self.attributes, text_type):
        self.attributes = eval(self.attributes)
    self.info = carddict['info']
    if isinstance(self.info, text_type):
        self.info = eval(self.info)
    return self