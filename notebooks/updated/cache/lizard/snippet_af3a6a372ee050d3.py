def _split_batches(self, data, batch_size):
    for i in range(0, len(data), batch_size):
        yield data[i:i + batch_size]