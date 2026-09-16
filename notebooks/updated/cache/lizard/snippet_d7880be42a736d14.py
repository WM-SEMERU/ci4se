def _system_path(self, subdir, basename=''):
    try:
        return self._file_path(os.path.join(self.system_dir, subdir), basename)
    except KeyboardInterrupt as e:
        raise e
    except Exception:
        return None