def get_subscriptions_by_subscriber_id(self, subscriber_id, max_results=10):
    return self.search_subscriptions(subscriber_id=subscriber_id,
        max_results=max_results)