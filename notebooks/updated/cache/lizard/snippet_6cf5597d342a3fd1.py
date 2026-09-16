def set_description(self, value: Union[Literal, Identifier, str], lang: str
    =None):
    return self.metadata.add(key=DC.description, value=value, lang=lang)