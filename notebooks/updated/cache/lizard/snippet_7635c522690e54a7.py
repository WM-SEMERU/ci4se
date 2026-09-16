def get_location(self):
    lat = None
    lon = None
    for _, _, o in self._graph.triples((None, GEO_NS.lat, None)):
        lat = float(o)
        break
    for _, _, o in self._graph.triples((None, GEO_NS.long, None)):
        lon = float(o)
        break
    return lat, lon