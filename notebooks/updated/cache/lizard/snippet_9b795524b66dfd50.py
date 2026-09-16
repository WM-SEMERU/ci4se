def assemble_chain(leaf, store):
    store_dict = {}
    for cert in store:
        store_dict[cert.get_subject().CN] = cert
    chain = [leaf]
    current = leaf
    try:
        while current.get_issuer().CN != current.get_subject().CN:
            chain.append(store_dict[current.get_issuer().CN])
            current = store_dict[current.get_issuer().CN]
    except KeyError:
        invalid = crypto.X509()
        patch_certificate(invalid)
        invalid.set_subject(current.get_issuer())
        chain.append(invalid)
    chain.reverse()
    return chain