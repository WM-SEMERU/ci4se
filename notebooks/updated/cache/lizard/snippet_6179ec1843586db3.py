def maybe_clean(self):
    now = time.time()
    if self.next_cleaning <= now:
        keys_to_delete = []
        for k, v in self.data.iteritems():
            if v.expiration <= now:
                keys_to_delete.append(k)
        for k in keys_to_delete:
            del self.data[k]
        now = time.time()
        self.next_cleaning = now + self.cleaning_interval