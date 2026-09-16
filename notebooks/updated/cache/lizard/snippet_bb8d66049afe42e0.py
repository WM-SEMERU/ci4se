def from_bin(class_, blob):
    f = io.BytesIO(blob)
    tx = class_.parse(f)
    try:
        tx.parse_unspents(f)
    except Exception:
        tx.unspents = []
    return tx