def get_space(self, space_key, expand='description.plain,homepage'):
    url = 'rest/api/space/{space_key}?expand={expand}'.format(space_key=
        space_key, expand=expand)
    return self.get(url)