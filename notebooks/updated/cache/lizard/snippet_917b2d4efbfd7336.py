def _generator_file(self):
    for path in self.paths:
        if os.path.isfile(path):
            if isvalid(path, self.access, self.extensions, minsize=self.minsize
                ):
                yield os.path.abspath(path)
        elif os.path.isdir(path):
            for root, _, fnames in self._walker(path):
                yield from self._generator_rebase(fnames, root)