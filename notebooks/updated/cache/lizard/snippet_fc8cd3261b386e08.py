def _write_init_fetchers(self, filenames):
    destination = '%s%s' % (self.output_directory, self.fetchers_path)
    self.write(destination=destination, filename='__init__.py',
        template_name='__init_fetcher__.py.tpl', filenames=self.
        _prepare_filenames(filenames, suffix='Fetcher'), class_prefix=self.
        _class_prefix, product_accronym=self._product_accronym, header=self
        .header_content)