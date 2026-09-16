def __add_scraped_requests_to_queue(self, queue_item, scraped_requests):
    new_queue_items = []
    for scraped_request in scraped_requests:
        HTTPRequestHelper.patch_with_options(scraped_request, self.
            __options, queue_item)
        if not HTTPRequestHelper.complies_with_scope(queue_item,
            scraped_request, self.__options.scope):
            continue
        if self.queue.has_request(scraped_request):
            continue
        scraped_request.depth = queue_item.request.depth + 1
        if self.__options.scope.max_depth is not None:
            if scraped_request.depth > self.__options.scope.max_depth:
                continue
        new_queue_item = self.queue.add_request(scraped_request)
        new_queue_items.append(new_queue_item)
    return new_queue_items