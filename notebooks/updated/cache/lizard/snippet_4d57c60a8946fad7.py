def set_page_property(self, page_id, data):
    url = 'rest/api/content/{page_id}/property'.format(page_id=page_id)
    json_data = data
    return self.post(path=url, data=json_data)