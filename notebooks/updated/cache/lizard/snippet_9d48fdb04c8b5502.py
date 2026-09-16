def getAsWmsDatasetString(self, session):
    FIRST_VALUE_INDEX = 12
    if type(self.raster) != type(None):
        valueGrassRasterString = self.getAsGrassAsciiGrid(session)
        values = valueGrassRasterString.split()
        wmsDatasetString = ''
        for i in range(FIRST_VALUE_INDEX, len(values)):
            wmsDatasetString += '{0:.6f}\r\n'.format(float(values[i]))
        return wmsDatasetString
    else:
        wmsDatasetString = self.rasterText