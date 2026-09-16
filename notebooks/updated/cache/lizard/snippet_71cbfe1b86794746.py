def equivalent_release_for_product(self, product):
    releases = self._default_manager.filter(version__startswith=self.
        major_version() + '.', channel=self.channel, product=product).order_by(
        '-version')
    if not getattr(settings, 'DEV', False):
        releases = releases.filter(is_public=True)
    if releases:
        return sorted(sorted(releases, reverse=True, key=lambda r: len(r.
            version.split('.'))), reverse=True, key=lambda r: r.version.
            split('.')[1])[0]