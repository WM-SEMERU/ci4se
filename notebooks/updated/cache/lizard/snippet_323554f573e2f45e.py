def get_channel(self, subscription_channel, **observer_params):
    keys = subscription_channel.get_routing_keys()
    self.watch_keys.add(frozenset({k_v[0] for key in keys for k_v in key}))
    self.create_route(subscription_channel, keys)
    subscription_channel._configure(self, self.connect_api, observer_params)
    return subscription_channel