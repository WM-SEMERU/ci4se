def get_view_items(self):
    view_items = [ViewItem(json_view_items, self.rest_client) for
        json_view_items in self.rest_client.make_request(self.viewItems)[
        'viewItems']]
    logger.debug('Retrieved ' + str(len(view_items)) + ' items from view ' +
        self.name)
    return view_items