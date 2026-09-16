def _blobs_page_start(iterator, page, response):
    page.prefixes = tuple(response.get('prefixes', ()))
    iterator.prefixes.update(page.prefixes)