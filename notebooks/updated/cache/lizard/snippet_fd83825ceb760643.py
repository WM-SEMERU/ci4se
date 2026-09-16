def close(self):
    if hasattr(self, 'iterators'):
        for it in self.iterators:
            if hasattr(it, 'close'):
                it.close()