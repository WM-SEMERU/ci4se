def _srcprob_app(self, xmlfile=None, overwrite=False, **kwargs):
    loglevel = kwargs.get('loglevel', self.loglevel)
    self.logger.log(loglevel, 'Computing src probability for component %s.',
        self.name)
    srcmdl_file = self.files['srcmdl']
    if xmlfile is not None:
        srcmdl_file = self.get_model_path(xmlfile)
    outfile = os.path.join(self.workdir,
        'ft1_srcprob{0[file_suffix]:s}.fits'.format(self.config))
    kw = dict(evfile=self.files['ft1'], scfile=self.data_files['scfile'],
        outfile=outfile, irfs=self.config['gtlike']['irfs'], srcmdl=srcmdl_file
        )
    self.logger.debug(kw)
    if os.path.isfile(outfile) and not overwrite:
        self.logger.info('Skipping gtsrcprob')
    else:
        run_gtapp('gtsrcprob', self.logger, kw, loglevel=loglevel)