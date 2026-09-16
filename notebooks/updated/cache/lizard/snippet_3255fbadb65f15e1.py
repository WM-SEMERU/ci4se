def recursive_include(self, dir, pattern):
    full_pattern = os.path.join(dir, '**', pattern)
    found = [f for f in glob(full_pattern, recursive=True) if not os.path.
        isdir(f)]
    self.extend(found)
    return bool(found)