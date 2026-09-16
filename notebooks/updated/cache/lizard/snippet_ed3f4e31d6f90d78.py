def __get_sub_rec(self, lpath):
    for d in lpath:
        root = self.get_path(d)
        if root is not None:
            yield d
        else:
            continue
        if not os.path.isdir(root):
            continue
        root = os.path.normpath(root)
        lend = len(root)
        for iwd in self._wmd.items():
            cur = iwd[1].path
            pref = os.path.commonprefix([root, cur])
            if root == os.sep or len(pref) == lend and len(cur) > lend and cur[
                lend] == os.sep:
                yield iwd[1].wd