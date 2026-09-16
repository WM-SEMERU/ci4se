def asn(self, as_number, **kwargs):
    indicator_obj = ASN(as_number, **kwargs)
    return self._indicator(indicator_obj)