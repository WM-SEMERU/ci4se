def get_bucket(self, key, rate=None, capacity=None, **kwargs):
    return buckets.Bucket(key=key, rate=rate or self.rate, capacity=
        capacity or self.capacity, storate=self.storate, **kwargs)