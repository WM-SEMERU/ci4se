def loader(path):
    finder = ModuleFinder if _isdir(path) else FileFinder
    return Loader(finder(path))