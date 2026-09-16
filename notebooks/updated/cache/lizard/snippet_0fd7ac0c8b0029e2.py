def matching_files(self):
    matching = []
    matcher = self.file_path_regex
    pieces = self.file_path_regex.pattern.split(sep)
    partial_matchers = list(map(re.compile, (sep.join(pieces[:i + 1]) for i in
        range(len(pieces)))))
    for root, dirs, files in walk(self.top_dir, topdown=True):
        for i in reversed(range(len(dirs))):
            dirname = relpath(join(root, dirs[i]), self.top_dir)
            dirlevel = dirname.count(sep)
            if not partial_matchers[dirlevel].match(dirname):
                del dirs[i]
        for filename in files:
            if matcher.match(filename):
                matching.append(abspath(join(root, filename)))
    return matching