def type(self):
    if self._device_mode == 1 or self._type == CertificateType.developer:
        return CertificateType.developer
    elif self._type == CertificateType.bootstrap:
        return CertificateType.bootstrap
    else:
        return CertificateType.lwm2m