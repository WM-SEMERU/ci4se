def find_root_thrifts(basedirs, sources, log=None):
    root_sources = set(sources)
    for source in sources:
        root_sources.difference_update(find_includes(basedirs, source, log=log)
            )
    return root_sources