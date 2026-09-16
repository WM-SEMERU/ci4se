def _fetch_next_block(self):
    fetched_items = self._fetch_items_helper_with_retries(self._fetch_function)
    while not fetched_items:
        if (self._collection_links and self._current_collection_index <
            self._collection_links_length):
            path = base.GetPathFromLink(self._collection_links[self.
                _current_collection_index], 'docs')
            collection_id = base.GetResourceIdOrFullNameFromLink(self.
                _collection_links[self._current_collection_index])
            self._continuation = None
            self._has_started = False

            def fetch_fn(options):
                return self._client.QueryFeed(path, collection_id, self.
                    _query, options)
            self._fetch_function = fetch_fn
            fetched_items = self._fetch_items_helper_with_retries(self.
                _fetch_function)
            self._current_collection_index += 1
        else:
            break
    return fetched_items