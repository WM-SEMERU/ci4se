def write_catalog(detections, fname, format='QUAKEML'):
    catalog = get_catalog(detections)
    catalog.write(filename=fname, format=format)