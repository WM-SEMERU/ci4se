def _tidy(self, work, file_path):
    output_file = os.path.join(self._output_dir, work)
    self._logger.info('Tidying file {} into {}'.format(file_path, output_file))
    try:
        tei_doc = etree.parse(file_path)
    except etree.XMLSyntaxError as err:
        self._logger.error('XML file "{}" is invalid: {}'.format(file_path,
            err))
        raise
    return self.transform(tei_doc).getroot()