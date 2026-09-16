def endswith(self, search_str):
    for entry in reversed(list(open(self._jrnl_file, 'r'))[-5:]):
        if search_str in entry:
            return True
    return False