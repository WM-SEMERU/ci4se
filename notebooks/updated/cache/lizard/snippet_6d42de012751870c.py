def get_leaf_certificates(certs):
    issuers = [cert.issuer.get_attributes_for_oid(x509.NameOID.COMMON_NAME) for
        cert in certs]
    leafs = [cert for cert in certs if cert.subject.get_attributes_for_oid(
        x509.NameOID.COMMON_NAME) not in issuers]
    return leafs