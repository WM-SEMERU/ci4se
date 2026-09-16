def get_rectangle(self, src):
    min_lon, min_lat, max_lon, max_lat = (self.integration_distance.
        get_affected_box(src))
    return (min_lon, min_lat), (max_lon - min_lon) % 360, max_lat - min_lat