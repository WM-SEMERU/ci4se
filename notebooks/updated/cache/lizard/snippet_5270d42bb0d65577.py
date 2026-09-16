def get_counter(self, name=None):
    return self.get_client(name=name, class_=statsd.Counter)