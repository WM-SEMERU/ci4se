def to_glyphs_blue_values(self, ufo, master):
    zones = []
    blue_values = _pairs(ufo.info.postscriptBlueValues)
    other_blues = _pairs(ufo.info.postscriptOtherBlues)
    for y1, y2 in blue_values:
        size = y2 - y1
        if y2 == 0:
            pos = 0
            size = -size
        else:
            pos = y1
        zones.append(self.glyphs_module.GSAlignmentZone(pos, size))
    for y1, y2 in other_blues:
        size = y1 - y2
        pos = y2
        zones.append(self.glyphs_module.GSAlignmentZone(pos, size))
    master.alignmentZones = sorted(zones, key=lambda zone: -zone.position)