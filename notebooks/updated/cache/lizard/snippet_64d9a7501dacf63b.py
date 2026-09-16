def walk(filesystem, top, topdown=True, onerror=None, followlinks=False):

    def do_walk(top_dir, top_most=False):
        top_dir = filesystem.normpath(top_dir)
        if not top_most and not followlinks and filesystem.islink(top_dir):
            return
        try:
            top_contents = _classify_directory_contents(filesystem, top_dir)
        except OSError as exc:
            top_contents = None
            if onerror is not None:
                onerror(exc)
        if top_contents is not None:
            if topdown:
                yield top_contents
            for directory in top_contents[1]:
                if not followlinks and filesystem.islink(directory):
                    continue
                for contents in do_walk(filesystem.joinpaths(top_dir,
                    directory)):
                    yield contents
            if not topdown:
                yield top_contents
    return do_walk(top, top_most=True)