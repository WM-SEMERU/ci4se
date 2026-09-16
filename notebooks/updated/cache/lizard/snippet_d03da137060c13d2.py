def _add_finder(importer, finder):
    existing_finder = _get_finder(importer)
    if not existing_finder:
        pkg_resources.register_finder(importer, finder)
    else:
        pkg_resources.register_finder(importer, ChainedFinder.of(
            existing_finder, finder))