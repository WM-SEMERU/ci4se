def _molfile(stream):
    yield MolfileStart()
    yield HeaderBlock(stream.popleft().strip(), stream.popleft().strip(),
        stream.popleft().strip())
    for token in _ctab(stream):
        yield token
    yield MolfileEnd()