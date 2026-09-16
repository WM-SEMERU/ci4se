def make_contexts(self, sites, rupture):
    sites, dctx = self.filter(sites, rupture)
    for param in (self.REQUIRES_DISTANCES - set([self.filter_distance])):
        distances = get_distances(rupture, sites, param)
        setattr(dctx, param, distances)
    reqv_obj = self.reqv.get(rupture.tectonic_region_type
        ) if self.reqv else None
    if reqv_obj and isinstance(rupture.surface, PlanarSurface):
        reqv = reqv_obj.get(dctx.repi, rupture.mag)
        if 'rjb' in self.REQUIRES_DISTANCES:
            dctx.rjb = reqv
        if 'rrup' in self.REQUIRES_DISTANCES:
            reqv_rup = numpy.sqrt(reqv ** 2 + rupture.hypocenter.depth ** 2)
            dctx.rrup = reqv_rup
    self.add_rup_params(rupture)
    sctx = SitesContext(self.REQUIRES_SITES_PARAMETERS, sites)
    return sctx, dctx