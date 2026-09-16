def get_absolute_url(self):
    try:
        return reverse('horizon:%s:%s:%s' % (self._registered_with.slug,
            self.slug, self.index_url_name))
    except Exception as exc:
        LOG.info('Error reversing absolute URL for %(self)s: %(exc)s', {
            'self': self, 'exc': exc})
        raise