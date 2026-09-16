def read_file(self, filepath, **kwargs):
    try:
        model = self._models[filepath]
    except KeyError:
        model = read_file(filepath, **kwargs)
        self._models[filepath] = model
        self.signalNewModelRead.emit(filepath)
    finally:
        self._paths_read.append(filepath)
    return self._models[filepath]