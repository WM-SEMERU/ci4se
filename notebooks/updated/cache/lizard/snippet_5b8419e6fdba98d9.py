def _walk(self):
    self._base_len = len(self.base)
    for base, dirs, files in os.walk(self.base, followlinks=self.follow_links):
        for name in dirs[:]:
            try:
                if not self._valid_folder(base, name):
                    dirs.remove(name)
            except Exception:
                dirs.remove(name)
                value = self.on_error(base, name)
                if value is not None:
                    yield value
            if self._abort:
                break
        if len(files):
            for name in files:
                try:
                    valid = self._valid_file(base, name)
                except Exception:
                    valid = False
                    value = self.on_error(base, name)
                    if value is not None:
                        yield value
                if valid:
                    yield self.on_match(base, name)
                else:
                    self._skipped += 1
                    value = self.on_skip(base, name)
                    if value is not None:
                        yield value
                if self._abort:
                    break
        if self._abort:
            break