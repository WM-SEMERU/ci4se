def _defineVariables(self):
    logger.info('Catalog contains %i objects' % len(self.data))
    mc_source_id_field = self.config['catalog']['mc_source_id_field']
    if mc_source_id_field is not None:
        if mc_source_id_field not in self.data.dtype.names:
            array = np.zeros(len(self.data), dtype='>i8')
            self.data = mlab.rec_append_fields(self.data, names=
                mc_source_id_field, arrs=array)
        logger.info('Found %i simulated objects' % np.sum(self.mc_source_id >
            0))