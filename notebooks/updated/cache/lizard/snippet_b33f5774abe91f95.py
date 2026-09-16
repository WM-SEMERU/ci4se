def _wrap(x, serializeFunc, encodeFunc=base64.urlsafe_b64encode, compress=True
    ):
    return encodeFunc(serializeFunc(x, compress))