def encrypt_file(src, dest, csv_keys):
    keys = massage_keys(csv_keys.split(','))
    cryptorito.encrypt(src, dest, keys)