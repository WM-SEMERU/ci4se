def text2lm(text, output_file, vocab_file=None, text2idngram_kwargs={},
    idngram2lm_kwargs={}):
    if vocab_file:
        used_vocab_file = vocab_file
    else:
        with tempfile.NamedTemporaryFile(suffix='.vocab', delete=False) as f:
            used_vocab_file = f.name
        text2vocab(text, used_vocab_file)
    with tempfile.NamedTemporaryFile(suffix='.idngram', delete=False) as f:
        idngram_file = f.name
    try:
        output1 = text2idngram(text, vocab_file=used_vocab_file,
            output_file=idngram_file, **text2idngram_kwargs)
        output2 = idngram2lm(idngram_file, vocab_file=used_vocab_file,
            output_file=output_file, **idngram2lm_kwargs)
    except ConversionError:
        output = None, None
        raise
    else:
        output = output1, output2
    finally:
        if not vocab_file:
            os.remove(used_vocab_file)
        os.remove(idngram_file)
    return output