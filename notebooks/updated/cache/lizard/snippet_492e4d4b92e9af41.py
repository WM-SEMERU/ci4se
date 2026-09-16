def register_finders():
    global __PREVIOUS_FINDER
    if __PREVIOUS_FINDER:
        return
    previous_finder = _get_finder(zipimport.zipimporter)
    assert previous_finder, 'This appears to be using an incompatible setuptools.'
    pkg_resources.register_finder(zipimport.zipimporter, ChainedFinder.of(
        pkg_resources.find_eggs_in_zip, find_wheels_in_zip))
    _add_finder(pkgutil.ImpImporter, find_wheels_on_path)
    if importlib_machinery is not None:
        _add_finder(importlib_machinery.FileFinder, find_wheels_on_path)
    __PREVIOUS_FINDER = previous_finder