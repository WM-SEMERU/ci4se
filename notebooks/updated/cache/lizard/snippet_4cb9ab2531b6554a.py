def could_be_unfinished_char(seq, encoding):
    if decodable(seq, encoding):
        return False
    if encodings.codecs.getdecoder('utf8') is encodings.codecs.getdecoder(
        encoding):
        return could_be_unfinished_utf8(seq)
    elif encodings.codecs.getdecoder('ascii') is encodings.codecs.getdecoder(
        encoding):
        return False
    else:
        return True