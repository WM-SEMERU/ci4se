def convert_data_array(arr, filter_func=None, converter_func=None):
    if filter_func:
        array = arr[filter_func(arr)]
    if converter_func:
        arr = converter_func(arr)
    return array