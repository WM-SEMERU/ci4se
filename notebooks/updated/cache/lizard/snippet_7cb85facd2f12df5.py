def add_tags(self, *tags):
    for _tag in tags:
        self.tags.get_or_create(name=_tag)