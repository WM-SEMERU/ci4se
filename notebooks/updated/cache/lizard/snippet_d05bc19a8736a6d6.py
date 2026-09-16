def get_pixel_bounds_from_datasec_keyword(datasec):
    datasec = re.findall('(\\d+)', datasec)
    x1 = min(int(datasec[0]), int(datasec[1]))
    x2 = max(int(datasec[0]), int(datasec[1]))
    y1 = min(int(datasec[2]), int(datasec[3]))
    y2 = max(int(datasec[2]), int(datasec[3]))
    return (x1, x2), (y1, y2)