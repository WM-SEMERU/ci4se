def recurse(self, root_path, dir_cb, listing_cb, max_listing_size=0,
    max_depth=MAX_REMOTE_RECURSION_DEPTH):
    q = deque([(root_path, 0)])
    collected = []

    def push_file(path, file_path, entry):
        collected.append((file_path, entry))
        if max_listing_size > 0 and len(collected) >= max_listing_size:
            listing_cb(path, collected)
            del collected[:]
    while q:
        path, current_depth = q.popleft()
        entries = self.listdir(path)
        for entry in entries:
            filename = stringify(entry.name)
            file_path = '%s/%s' % (path, filename)
            if entry.is_symlink:
                push_file(path, file_path, entry)
            elif entry.is_directory:
                if filename == '.' or filename == '..':
                    continue
                if dir_cb is not None:
                    dir_cb(path, file_path, entry)
                new_depth = current_depth + 1
                if max_depth is None or new_depth <= max_depth:
                    q.append((file_path, new_depth))
            elif entry.is_regular:
                if listing_cb is not None:
                    push_file(path, file_path, entry)
    if listing_cb is not None and (max_listing_size == 0 or len(collected) > 0
        ):
        listing_cb(path, collected)