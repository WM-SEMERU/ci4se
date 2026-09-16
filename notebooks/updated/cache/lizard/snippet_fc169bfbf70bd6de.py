def _read(self, directory, filename, session, path, name, extension,
    spatial, spatialReferenceID, replaceParamFile):
    self.fileExtension = extension
    with open(path, 'r') as f:
        for line in f:
            sline = line.strip().split()
            if len(sline) == 1:
                self.numLocations = sline[0]
            else:
                location = OutputLocation(linkOrCellI=sline[0], nodeOrCellJ
                    =sline[1])
                location.outputLocationFile = self