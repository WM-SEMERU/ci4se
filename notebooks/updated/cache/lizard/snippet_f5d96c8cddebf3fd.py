def get_dependency(self, worker_ctx):
    extra_headers = self.get_message_headers(worker_ctx)

    def dispatch(event_type, event_data):
        self.publisher.publish(event_data, exchange=self.exchange,
            routing_key=event_type, extra_headers=extra_headers)
    return dispatch