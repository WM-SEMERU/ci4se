def array2bytes(arr, bytes_type=bytes):
    bio = io.BytesIO()
    np.save(bio, arr, allow_pickle=False)
    return bytes_type(bio.getvalue())