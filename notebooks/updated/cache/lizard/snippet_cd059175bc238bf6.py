def _writeSic(self, filelike, specfile, compress):
    aux.writeJsonZipfile(filelike, self.sic[specfile], compress)