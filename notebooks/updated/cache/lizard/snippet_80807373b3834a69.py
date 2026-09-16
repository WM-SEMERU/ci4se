def InputCodon(seq_length, ignore_stop_codons=True, name=None, **kwargs):
    if ignore_stop_codons:
        vocab = CODONS
    else:
        vocab = CODONS + STOP_CODONS
    assert seq_length % 3 == 0
    return Input((seq_length / 3, len(vocab)), name=name, **kwargs)