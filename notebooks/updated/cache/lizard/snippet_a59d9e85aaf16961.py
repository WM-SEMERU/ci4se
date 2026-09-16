def cd_previous(self):
    if self._prev_dir is None or isinstance(self._prev_dir, ROOT.TROOT):
        return False
    if isinstance(self._prev_dir, ROOT.TFile):
        if self._prev_dir.IsOpen() and self._prev_dir.IsWritable():
            self._prev_dir.cd()
            return True
        return False
    if not self._prev_dir.IsWritable():
        return False
    prev_file = self._prev_dir.GetFile()
    if prev_file and prev_file.IsOpen():
        self._prev_dir.cd()
        return True
    return False