def try_open(self, null_if_noexist=False, **kwargs):
    try:
        return self.open(**kwargs)
    except IOError as e:
        if e.errno == 2:
            if null_if_noexist:
                import io, os
                return io.open(os.devnull, **kwargs)
            return None
        raise