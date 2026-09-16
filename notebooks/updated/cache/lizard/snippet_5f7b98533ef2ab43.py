def clear_validation(self, cert):
    if cert.signature in self._validate_map:
        del self._validate_map[cert.signature]