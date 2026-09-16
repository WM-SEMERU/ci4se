def array_equiv(arr1, arr2):
    arr1, arr2 = as_like_arrays(arr1, arr2)
    if arr1.shape != arr2.shape:
        return False
    with warnings.catch_warnings():
        warnings.filterwarnings('ignore', "In the future, 'NAT == x'")
        flag_array = arr1 == arr2
        flag_array |= isnull(arr1) & isnull(arr2)
        return bool(flag_array.all())