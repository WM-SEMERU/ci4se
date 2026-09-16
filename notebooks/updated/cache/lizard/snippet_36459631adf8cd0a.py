def insert(self, item, priority):
    with self.lock:
        self_data = self.data
        rotate = self_data.rotate
        self_items = self.items
        maxlen = self._maxlen
        try:
            if priority <= self_data[-1][1]:
                self_data.append((item, priority))
            elif priority > self_data[0][1]:
                self_data.appendleft((item, priority))
            else:
                length = len(self_data) + 1
                mid = length // 2
                shift = 0
                while True:
                    if priority <= self_data[0][1]:
                        rotate(-mid)
                        shift += mid
                        mid //= 2
                        if mid == 0:
                            mid += 1
                    else:
                        rotate(mid)
                        shift -= mid
                        mid //= 2
                        if mid == 0:
                            mid += 1
                    if self_data[-1][1] >= priority > self_data[0][1]:
                        self_data.appendleft((item, priority))
                        if shift > length // 2:
                            shift = length % shift
                            rotate(-shift)
                        else:
                            rotate(shift)
                        break
            try:
                self_items[item] += 1
            except TypeError:
                self_items[repr(item)] += 1
        except IndexError:
            self_data.append((item, priority))
            try:
                self_items[item] = 1
            except TypeError:
                self_items[repr(item)] = 1
        if maxlen is not None and maxlen < len(self_data):
            self._poplast()