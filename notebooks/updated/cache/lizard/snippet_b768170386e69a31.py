def add(self, parent, obj_type, **attributes):
    response = self.post(self.server_url + parent.ref + '/' + obj_type,
        attributes)
    return self._get_href(response.json())