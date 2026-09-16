def split_file_urls_by_size(self, size):
    large_items = []
    small_items = []
    for file_url in self.file_urls:
        if file_url.size >= size:
            large_items.append(file_url)
        else:
            small_items.append(file_url)
    return large_items, small_items