def _clean_item(self, item):
    item_copy = dict(item)
    del item_copy['body']
    del item_copy['links']
    del item_copy['response_headers']
    del item_copy['request_headers']
    del item_copy['status_code']
    del item_copy['status_msg']
    item_copy['action'] = 'ack'
    item_copy['logger'] = self.logger.name
    item_copy
    return item_copy