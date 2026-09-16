def save(self, indexes, parent_id):
    if self.content():
        parent = Page.objects.get(id=parent_id)
        response = requests.get(self._base_url + API_PAGES_ENDPOINT + str(
            indexes[0]) + '/')
        section_page = response.json()
        self.process_child_section(section_page['id'], parent)