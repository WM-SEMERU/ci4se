def to_gds(self, multiplier):
    data = []
    for ii in range(len(self.polygons)):
        if len(self.polygons[ii]) > 4094:
            raise ValueError(
                '[GDSPY] Polygons with more than 4094 are not supported by the GDSII format.'
                )
        data.append(struct.pack('>10h', 4, 2048, 6, 3330, self.layers[ii], 
            6, 3586, self.datatypes[ii], 12 + 8 * len(self.polygons[ii]), 4099)
            )
        data.extend(struct.pack('>2l', int(round(point[0] * multiplier)),
            int(round(point[1] * multiplier))) for point in self.polygons[ii])
        data.append(struct.pack('>2l2h', int(round(self.polygons[ii][0][0] *
            multiplier)), int(round(self.polygons[ii][0][1] * multiplier)),
            4, 4352))
    return b''.join(data)