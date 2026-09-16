def _Aff4Read(aff4_obj, offset, length):
    length = length or _Aff4Size(aff4_obj) - offset
    aff4_obj.Seek(offset)
    return aff4_obj.Read(length)