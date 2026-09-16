def add_geo_facet(self, *args, **kwargs):
    self.facets.append(GeoDistanceFacet(*args, **kwargs))