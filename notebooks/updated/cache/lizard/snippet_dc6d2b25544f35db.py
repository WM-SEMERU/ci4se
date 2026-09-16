def read_shakemap(self, haz_sitecol, assetcol):
    oq = self.oqparam
    E = oq.number_of_ground_motion_fields
    oq.risk_imtls = oq.imtls or self.datastore.parent['oqparam'].imtls
    extra = self.riskmodel.get_extra_imts(oq.risk_imtls)
    if extra:
        logging.warning(
            'There are risk functions for not available IMTs which will be ignored: %s'
             % extra)
    logging.info('Getting/reducing shakemap')
    with self.monitor('getting/reducing shakemap'):
        smap = oq.shakemap_id if oq.shakemap_id else numpy.load(oq.inputs[
            'shakemap'])
        sitecol, shakemap, discarded = get_sitecol_shakemap(smap, oq.imtls,
            haz_sitecol, oq.asset_hazard_distance['default'], oq.discard_assets
            )
        if len(discarded):
            self.datastore['discarded'] = discarded
        assetcol = assetcol.reduce_also(sitecol)
    logging.info('Building GMFs')
    with self.monitor('building/saving GMFs'):
        imts, gmfs = to_gmfs(shakemap, oq.spatial_correlation, oq.
            cross_correlation, oq.site_effects, oq.truncation_level, E, oq.
            random_seed, oq.imtls)
        save_gmf_data(self.datastore, sitecol, gmfs, imts)
    return sitecol, assetcol