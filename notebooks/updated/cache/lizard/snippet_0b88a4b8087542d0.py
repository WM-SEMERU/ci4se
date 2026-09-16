def get_area_def(self, dsid):
    geocoding = self.root.find('.//Tile_Geocoding')
    epsg = geocoding.find('HORIZONTAL_CS_CODE').text
    rows = int(geocoding.find('Size[@resolution="' + str(dsid.resolution) +
        '"]/NROWS').text)
    cols = int(geocoding.find('Size[@resolution="' + str(dsid.resolution) +
        '"]/NCOLS').text)
    geoposition = geocoding.find('Geoposition[@resolution="' + str(dsid.
        resolution) + '"]')
    ulx = float(geoposition.find('ULX').text)
    uly = float(geoposition.find('ULY').text)
    xdim = float(geoposition.find('XDIM').text)
    ydim = float(geoposition.find('YDIM').text)
    area_extent = ulx, uly + rows * ydim, ulx + cols * xdim, uly
    area = geometry.AreaDefinition(self.tile, 'On-the-fly area', self.tile,
        {'init': epsg}, cols, rows, area_extent)
    return area