def _verify_arguments(self, kwargs):
    geom_stat_args = kwargs.keys() | self._stat._kwargs.keys()
    unknown = geom_stat_args - self.aesthetics() - self.DEFAULT_PARAMS.keys(
        ) - self._stat.aesthetics() - self._stat.DEFAULT_PARAMS.keys() - {
        'data', 'mapping', 'show_legend', 'inherit_aes'}
    if unknown:
        msg = (
            'Parameters {}, are not understood by either the geom, stat or layer.'
            )
        raise PlotnineError(msg.format(unknown))