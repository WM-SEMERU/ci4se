def _get_k_p_a(font, left, right):
    chars = left + right
    args = [None, 1, cf.kCFTypeDictionaryKeyCallBacks, cf.
        kCFTypeDictionaryValueCallBacks]
    attributes = cf.CFDictionaryCreateMutable(*args)
    cf.CFDictionaryAddValue(attributes, kCTFontAttributeName, font)
    string = cf.CFAttributedStringCreate(None, CFSTR(chars), attributes)
    typesetter = ct.CTTypesetterCreateWithAttributedString(string)
    cf.CFRelease(string)
    cf.CFRelease(attributes)
    range = CFRange(0, 1)
    line = ct.CTTypesetterCreateLine(typesetter, range)
    offset = ct.CTLineGetOffsetForStringIndex(line, 1, None)
    cf.CFRelease(line)
    cf.CFRelease(typesetter)
    return offset