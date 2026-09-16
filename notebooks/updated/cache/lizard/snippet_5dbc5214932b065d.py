def move_bulk(self, from_statuses, to_status):
    for status in from_statuses:
        from_status_items = self.__get_var('items_' + status)
        self.__set_var('items_' + status, OrderedDict())
        to_status_items = self.__get_var('items_' + to_status)
        to_status_items.update(from_status_items)