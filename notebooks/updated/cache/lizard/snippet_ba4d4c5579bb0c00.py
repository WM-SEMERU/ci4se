def get_item_list_by_name(self, item_list_name, category='own'):
    resp = self.api_request('/item_lists')
    for item_list in resp[category]:
        if item_list['name'] == item_list_name:
            return self.get_item_list(item_list['item_list_url'])
    raise ValueError('List does not exist: ' + item_list_name)