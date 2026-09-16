def _next_page(self):
    if not self._has_next_page():
        return None
    if self.next_page_token is not None:
        setattr(self._request, self._request_token_field, self.next_page_token)
    response = self._method(self._request)
    self.next_page_token = getattr(response, self._response_token_field)
    items = getattr(response, self._items_field)
    page = Page(self, items, self.item_to_value)
    return page