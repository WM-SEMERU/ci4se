def remove_rate_limit(self, limiter):
    if limiter in self.rate_limiters:
        self.unsubscribe('capacity', limiter.on_capacity)
        self.rate_limiters.remove(limiter)