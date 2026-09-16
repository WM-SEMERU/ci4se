def cert(self):
    if self.cert_files is not None:
        return self.cert_files
    certs = self.certs or '/certs/'
    ssl_path = os.path.join(os.pardir, certs)
    try:
        cert_path = os.listdir(ssl_path)
    except FileNotFoundError:
        raise CertsError(certs)
    except OSError:
        raise CertsError(certs)
    cert = None
    key = None
    for file in cert_path:
        ext = os.path.splitext(file)[-1]
        if ext in ['.crt', '.cert']:
            cert = os.path.join(ssl_path, file)
        elif ext == '.key':
            key = os.path.join(ssl_path, file)
    if cert is None or key is None:
        raise CertsError(certs)
    return [cert, key]