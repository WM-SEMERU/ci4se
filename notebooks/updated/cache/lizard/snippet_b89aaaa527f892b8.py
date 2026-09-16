def relpath(self, path):
    for root in self.roots:
        if isinstance(root, Pattern):
            match = root.match(path)
            if not match:
                continue
            root = match.group(0)
        try:
            relative = path.split(root, 1)[1]
            return relative.lstrip('/')
        except IndexError:
            continue
    return path