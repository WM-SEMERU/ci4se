def get_file(f, decoder, read):
    with f as f:
        if decoder is None:
            return list(f)
        else:
            d = f.read() if read else f
            out = decoder(d)
            if isinstance(out, (tuple, list)):
                return out
            else:
                return [out]