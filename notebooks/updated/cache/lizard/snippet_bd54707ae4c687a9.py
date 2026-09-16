def AddItem(self, item, f=lambda x: x):
    with self._mutex:
        if len(self.items) < self._max_size or self._max_size == 0:
            self.items.append(f(item))
        else:
            r = self._random.randint(0, self._num_items_seen)
            if r < self._max_size:
                self.items.pop(r)
                self.items.append(f(item))
            elif self.always_keep_last:
                self.items[-1] = f(item)
        self._num_items_seen += 1