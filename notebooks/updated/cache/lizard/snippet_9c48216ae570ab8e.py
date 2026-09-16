def demeshgrid(arr):
    dim = len(arr.shape)
    for i in range(dim):
        Slice1 = [0] * dim
        Slice2 = [1] * dim
        Slice1[i] = slice(None)
        Slice2[i] = slice(None)
        if (arr[tuple(Slice1)] == arr[tuple(Slice2)]).all():
            return arr[tuple(Slice1)]