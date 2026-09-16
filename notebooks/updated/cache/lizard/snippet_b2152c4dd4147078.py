def read_exposure(self, haz_sitecol=None):
    with self.monitor('reading exposure', autoflush=True):
        self.sitecol, self.assetcol, discarded = (readinput.
            get_sitecol_assetcol(self.oqparam, haz_sitecol, self.riskmodel.
            loss_types))
        if len(discarded):
            self.datastore['discarded'] = discarded
            if hasattr(self, 'rup'):
                logging.info(
                    '%d assets were discarded because too far from the rupture; use `oq show discarded` to show them and `oq plot_assets` to plot them'
                     % len(discarded))
            elif not self.oqparam.discard_assets:
                self.datastore['sitecol'] = self.sitecol
                self.datastore['assetcol'] = self.assetcol
                raise RuntimeError(
                    '%d assets were discarded; use `oq show discarded` to show them and `oq plot_assets` to plot them'
                     % len(discarded))
    taxonomies = set(taxo for taxo in self.assetcol.tagcol.taxonomy if taxo !=
        '?')
    if len(self.riskmodel.taxonomies) > len(taxonomies):
        logging.info('Reducing risk model from %d to %d taxonomies', len(
            self.riskmodel.taxonomies), len(taxonomies))
        self.riskmodel = self.riskmodel.reduce(taxonomies)
    return readinput.exposure