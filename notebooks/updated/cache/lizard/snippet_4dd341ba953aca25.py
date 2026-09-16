def _get_openstack_release(self):
    for i, os_pair in enumerate(OPENSTACK_RELEASES_PAIRS):
        setattr(self, os_pair, i)
    releases = {('trusty', None): self.trusty_icehouse, ('trusty',
        'cloud:trusty-kilo'): self.trusty_kilo, ('trusty',
        'cloud:trusty-liberty'): self.trusty_liberty, ('trusty',
        'cloud:trusty-mitaka'): self.trusty_mitaka, ('xenial', None): self.
        xenial_mitaka, ('xenial', 'cloud:xenial-newton'): self.
        xenial_newton, ('xenial', 'cloud:xenial-ocata'): self.xenial_ocata,
        ('xenial', 'cloud:xenial-pike'): self.xenial_pike, ('xenial',
        'cloud:xenial-queens'): self.xenial_queens, ('yakkety', None): self
        .yakkety_newton, ('zesty', None): self.zesty_ocata, ('artful', None
        ): self.artful_pike, ('bionic', None): self.bionic_queens, (
        'bionic', 'cloud:bionic-rocky'): self.bionic_rocky, ('bionic',
        'cloud:bionic-stein'): self.bionic_stein, ('cosmic', None): self.
        cosmic_rocky, ('disco', None): self.disco_stein}
    return releases[self.series, self.openstack]