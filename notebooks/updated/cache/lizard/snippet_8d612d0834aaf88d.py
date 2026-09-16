def hashid_arr(arr, label='arr', hashlen=16):
    hashstr = hash_data(arr)[0:hashlen]
    if isinstance(arr, (list, tuple)):
        shapestr = len(arr)
    else:
        shapestr = ','.join(list(map(str, arr.shape)))
    hashid = '{}-{}-{}'.format(label, shapestr, hashstr)
    return hashid