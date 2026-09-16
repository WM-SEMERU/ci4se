def do_add_signature(input_file, output_file, signature_file):
    signature = open(signature_file, 'rb').read()
    if len(signature) == 256:
        hash_algo = 'sha1'
    elif len(signature) == 512:
        hash_algo = 'sha384'
    else:
        raise ValueError()
    with open(output_file, 'w+b') as dst:
        with open(input_file, 'rb') as src:
            add_signature_block(src, dst, hash_algo, signature)