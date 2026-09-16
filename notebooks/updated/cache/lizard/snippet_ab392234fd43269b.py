def list_instances(self, filter_='', page_size=None, page_token=None):
    metadata = _metadata_with_prefix(self.project_name)
    path = 'projects/%s' % (self.project,)
    page_iter = self.instance_admin_api.list_instances(path, page_size=
        page_size, metadata=metadata)
    page_iter.item_to_value = self._item_to_instance
    page_iter.next_page_token = page_token
    return page_iter