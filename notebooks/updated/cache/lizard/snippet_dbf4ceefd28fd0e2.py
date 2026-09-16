def _read(self, directory, filename, session, path, name, extension,
    spatial, spatialReferenceID, replaceParamFile):
    self.fileExtension = extension
    with open(path, 'r') as hmetFile:
        for line in hmetFile:
            sline = line.strip().split()
            try:
                dateTime = datetime(int(sline[0]), int(sline[1]), int(sline
                    [2]), int(sline[3]))
                hmetRecord = HmetRecord(hmetDateTime=dateTime,
                    barometricPress=sline[4], relHumidity=sline[5],
                    totalSkyCover=sline[6], windSpeed=sline[7], dryBulbTemp
                    =sline[8], directRad=sline[9], globalRad=sline[10])
                hmetRecord.hmetFile = self
            except:
                pass