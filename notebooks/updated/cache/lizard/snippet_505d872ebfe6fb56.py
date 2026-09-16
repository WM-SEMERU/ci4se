def get_total_size(self, entries):
    size = 0
    for entry in entries:
        if entry['response']['bodySize'] > 0:
            size += entry['response']['bodySize']
    return size