def remove(self, index):
    assert index < self.count
    last_index = self.count - 1
    data = self.get(index)
    if index == last_index:
        last_data = data
        moved = None
    else:
        last_data = self.get(last_index)
        data[0:self.chunk_size] = last_data
        moved = last_index
    last_data[0:self.chunk_size] = [0] * self.chunk_size
    self.count -= 1
    return moved