def parse_certificates(data, password):
    if is_pem(data):
        certs = []
        for cert in data.split(PEM_IDENTIFIER):
            try:
                certs.append(x509.load_pem_x509_certificate(PEM_IDENTIFIER +
                    cert, default_backend()))
            except Exception:
                pass
        if len(certs) > 0:
            return certs
    if is_pkcs12(data):
        try:
            p12 = crypto.load_pkcs12(data, password)
            data = crypto.dump_certificate(crypto.FILETYPE_PEM, p12.
                get_certificate())
            return [x509.load_pem_x509_certificate(data, default_backend())]
        except crypto.Error as e:
            raise ValueError(e)
    try:
        return [x509.load_der_x509_certificate(data, default_backend())]
    except Exception:
        pass
    raise ValueError('Could not parse certificate.')