def add_request(self, request):
    queue_item = QueueItem(request, Response(request.url))
    self.add(queue_item)
    return queue_item