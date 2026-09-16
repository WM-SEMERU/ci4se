def remove(name, keystore, passphrase):
    certs_list = []
    keystore_object = jks.KeyStore.load(keystore, passphrase)
    for alias, loaded_cert in keystore_object.entries.items():
        if name not in alias:
            certs_list.append(loaded_cert)
    if len(keystore_object.entries) != len(certs_list):
        keystore_object = jks.KeyStore.new('jks', certs_list)
        keystore_object.save(keystore, passphrase)
        return True
    else:
        return False