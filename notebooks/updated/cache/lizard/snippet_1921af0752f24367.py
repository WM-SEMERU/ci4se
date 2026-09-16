def get_raw(self, name=None):
    return self.get_client(name=name, class_=statsd.Raw)