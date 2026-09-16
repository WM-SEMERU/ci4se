def linkify(buildroot, s, memoized_urls):

    def memoized_to_url(m):
        value = memoized_urls.get(m.group(0), _NO_URL)
        if value is _NO_URL:
            value = to_url(m)
            memoized_urls[m.group(0)] = value
        return value

    def to_url(m):
        if m.group(1):
            return m.group(0)
        path = m.group(0)
        if path.startswith('/'):
            path = os.path.relpath(path, buildroot)
        elif path.startswith('..'):
            return None
        else:
            parts = path.split(':')
            if len(parts) == 2:
                putative_dir = parts[0]
            else:
                putative_dir = path
            if os.path.isdir(os.path.join(buildroot, putative_dir)):
                build_files = list(BuildFile.get_build_files_family(
                    FileSystemProjectTree(buildroot), putative_dir))
                if build_files:
                    path = build_files[0].relpath
                else:
                    return None
        if os.path.exists(os.path.join(buildroot, path)):
            return '/browse/{}'.format(path)
        else:
            return None

    def maybe_add_link(url, text):
        return '<a target="_blank" href="{}">{}</a>'.format(url, text
            ) if url else text
    return _PATH_RE.sub(lambda m: maybe_add_link(memoized_to_url(m), m.
        group(0)), s)