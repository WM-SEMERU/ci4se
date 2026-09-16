def cast_to_seq(obj, alphabet=IUPAC.extended_protein):
    if isinstance(obj, Seq):
        return obj
    if isinstance(obj, SeqRecord):
        return obj.seq
    if isinstance(obj, str):
        obj = obj.upper()
        return Seq(obj, alphabet)
    else:
        raise ValueError('Must provide a string, Seq, or SeqRecord object.')