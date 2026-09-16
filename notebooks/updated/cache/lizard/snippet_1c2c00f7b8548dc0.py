def statistics(self, start=None, end=None, namespace=None):
    return self.make_context(start=start, end=end, namespace=namespace
        ).statistics()