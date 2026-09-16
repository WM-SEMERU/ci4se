def blob_to_pyasn1(blob):
    return pyasn1.codec.der.decoder.decode(blob, asn1Spec=pyasn1_modules.
        rfc2459.Certificate())[0]