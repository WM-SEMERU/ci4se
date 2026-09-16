def _load_raster_text(self, raster_path):
    with open(raster_path, 'r') as f:
        self.rasterText = f.read()
    lines = self.rasterText.split('\n')
    for line in lines[0:6]:
        spline = line.split()
        if 'north' in spline[0].lower():
            self.north = float(spline[1])
        elif 'south' in spline[0].lower():
            self.south = float(spline[1])
        elif 'east' in spline[0].lower():
            self.east = float(spline[1])
        elif 'west' in spline[0].lower():
            self.west = float(spline[1])
        elif 'rows' in spline[0].lower():
            self.rows = int(spline[1])
        elif 'cols' in spline[0].lower():
            self.columns = int(spline[1])