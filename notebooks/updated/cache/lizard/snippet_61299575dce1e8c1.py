def rowmap(table, rowmapper, header, failonerror=False):
    return RowMapView(table, rowmapper, header, failonerror=failonerror)