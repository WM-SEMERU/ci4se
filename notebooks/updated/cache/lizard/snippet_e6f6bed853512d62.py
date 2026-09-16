def in_cache(self, objpath, metahash):
    try:
        self.path_in_cache(objpath, metahash)
        return True
    except CacheMiss:
        return False