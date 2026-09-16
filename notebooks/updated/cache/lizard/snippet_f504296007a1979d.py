def Flush(self):
    self.data_store.StoreRequestsAndResponses(new_requests=self.
        request_queue, new_responses=self.response_queue,
        requests_to_delete=self.requests_to_delete)
    mutation_pool = self.data_store.GetMutationPool()
    with mutation_pool:
        messages_by_queue = collection.Group(list(itervalues(self.
            client_messages_to_delete)), lambda request: request.queue)
        for queue, messages in iteritems(messages_by_queue):
            self.Delete(queue, messages, mutation_pool=mutation_pool)
        if self.new_client_messages:
            for timestamp, messages in iteritems(collection.Group(self.
                new_client_messages, lambda x: x[1])):
                self.Schedule([x[0] for x in messages], timestamp=timestamp,
                    mutation_pool=mutation_pool)
    if self.notifications:
        for notification in itervalues(self.notifications):
            self.NotifyQueue(notification, mutation_pool=mutation_pool)
        mutation_pool.Flush()
    self.request_queue = []
    self.response_queue = []
    self.requests_to_delete = []
    self.client_messages_to_delete = {}
    self.notifications = {}
    self.new_client_messages = []