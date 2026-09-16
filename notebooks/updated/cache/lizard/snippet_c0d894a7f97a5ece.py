def chunks(arr, size):
    for i in _range(0, len(arr), size):
        yield arr[i:i + size]