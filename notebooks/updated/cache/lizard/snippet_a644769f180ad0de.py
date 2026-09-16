def split(self, bits_count):
    result = []
    array = WBinArray(self.__value, self.__size)
    if len(array) % bits_count > 0:
        array.resize(len(array) + (bits_count - len(array) % bits_count))
    while len(array):
        result.append(WBinArray(array[:bits_count], bits_count))
        array = array[bits_count:]
    return result