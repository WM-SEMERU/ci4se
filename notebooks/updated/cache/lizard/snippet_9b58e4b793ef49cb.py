def rotated(self, angle_degrees_ccw):
    angle = angle_degrees_ccw / 180.0 * pi
    c, s = cos(angle), sin(angle)
    return self @ PdfMatrix((c, s, -s, c, 0, 0))