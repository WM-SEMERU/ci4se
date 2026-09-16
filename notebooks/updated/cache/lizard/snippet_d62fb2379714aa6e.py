def hashstr(data, hashlen=HASH_LEN, alphabet=ALPHABET):
    if util_type.HAVE_NUMPY and isinstance(data, np.ndarray):
        if data.dtype.kind == 'O':
            msg = '[ut] hashing ndarrays with dtype=object is unstable'
            warnings.warn(msg, RuntimeWarning)
            data = data.dumps()
    if isinstance(data, tuple):
        if False:
            hasher = hashlib.sha512()
            items = data
            for item in items:
                if isinstance(item, uuid.UUID):
                    hasher.update(item.bytes)
                else:
                    hasher.update(item)
            text = hasher.hexdigest()
            hashstr2 = convert_hexstr_to_bigbase(text, alphabet, bigbase=
                len(alphabet))
            text = hashstr2[:hashlen]
            return text
        else:
            msg = '[ut] hashing tuples with repr is not a good idea. FIXME'
            data = repr(data)
    if isinstance(data, six.text_type):
        data = data.encode('utf-8')
    if isinstance(data, stringlike) and len(data) == 0:
        text = alphabet[0] * hashlen
    else:
        text = hashlib.sha512(data).hexdigest()
        hashstr2 = convert_hexstr_to_bigbase(text, alphabet, bigbase=len(
            alphabet))
        text = hashstr2[:hashlen]
    return text