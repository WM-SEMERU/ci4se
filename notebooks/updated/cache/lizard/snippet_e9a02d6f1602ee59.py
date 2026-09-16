def set_attributes(self, attributes):
    self.attributes = attributes
    for attribute, value in attributes.items():
        self.__setattr__(attribute, value)
        if DATE_PATTERN.match(text_type(value)):
            naive = datetime.strptime(value, '%Y-%m-%dT%H:%M:%SZ')
            aware = naive.replace(tzinfo=pytz.utc)
            self.__setattr__(attribute + '_date', aware)