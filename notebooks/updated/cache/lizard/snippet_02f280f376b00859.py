def parse_region(self, include, region_type, region_end, line):
    if self.coordsys is None:
        raise DS9RegionParserError(
            'No coordinate system specified and a region has been found.')
    else:
        helper = DS9RegionParser(coordsys=self.coordsys, include=include,
            region_type=region_type, region_end=region_end, global_meta=
            self.global_meta, line=line)
        helper.parse()
        self.shapes.append(helper.shape)