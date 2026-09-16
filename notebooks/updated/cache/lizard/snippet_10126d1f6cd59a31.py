def read_cert_from_file(cert_file, cert_type):
    if not cert_file:
        return ''
    if cert_type == 'pem':
        _a = read_file(cert_file, 'rb').decode()
        _b = _a.replace('\r\n', '\n')
        lines = _b.split('\n')
        for pattern in ('-----BEGIN CERTIFICATE-----',
            '-----BEGIN PUBLIC KEY-----'):
            if pattern in lines:
                lines = lines[lines.index(pattern) + 1:]
                break
        else:
            raise CertificateError('Strange beginning of PEM file')
        for pattern in ('-----END CERTIFICATE-----', '-----END PUBLIC KEY-----'
            ):
            if pattern in lines:
                lines = lines[:lines.index(pattern)]
                break
        else:
            raise CertificateError('Strange end of PEM file')
        return make_str(''.join(lines).encode())
    if cert_type in ['der', 'cer', 'crt']:
        data = read_file(cert_file, 'rb')
        _cert = base64.b64encode(data)
        return make_str(_cert)