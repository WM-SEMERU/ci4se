def _get_choices(self, gandi):
    packages = super(CertificatePackageType, self)._get_choices(gandi)
    return list(set([pack.split('_')[1] for pack in packages]))