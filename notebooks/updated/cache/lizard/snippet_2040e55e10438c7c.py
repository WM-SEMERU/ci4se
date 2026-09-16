def length(self):
    return math.sqrt((self.endpoint_a.northing - self.endpoint_b.northing) **
        2 + (self.endpoint_a.easting - self.endpoint_b.easting) ** 2)