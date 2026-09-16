def merge_conflicts(self):
    filenames = set()
    listing = self.context.capture('git', 'ls-files', '--unmerged', '-z')
    for entry in split(listing, '\x00'):
        metadata, _, name = entry.partition('\t')
        if metadata and name:
            filenames.add(name)
    return sorted(filenames)