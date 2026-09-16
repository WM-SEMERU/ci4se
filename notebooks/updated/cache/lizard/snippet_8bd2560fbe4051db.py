def set_creator(self, value: Union[Literal, Identifier, str], lang: str=None):
    self.metadata.add(key=DC.creator, value=value, lang=lang)