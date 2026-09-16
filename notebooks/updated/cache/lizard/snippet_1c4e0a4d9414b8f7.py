def do_list(marfile, detailed=False):
    with open(marfile, 'rb') as f:
        with MarReader(f) as m:
            if detailed:
                if m.compression_type:
                    yield 'Compression type: {}'.format(m.compression_type)
                if m.signature_type:
                    yield 'Signature type: {}'.format(m.signature_type)
                if m.mardata.signatures:
                    plural = ('s' if m.mardata.signatures.count == 0 or m.
                        mardata.signatures.count > 1 else '')
                    yield 'Signature block found with {} signature{}'.format(m
                        .mardata.signatures.count, plural)
                    for s in m.mardata.signatures.sigs:
                        yield '- Signature {} size {}'.format(s.
                            algorithm_id, s.size)
                    yield ''
                if m.mardata.additional:
                    yield '{} additional block found:'.format(len(m.mardata
                        .additional.sections))
                    for s in m.mardata.additional.sections:
                        if s.id == 1:
                            yield '  - Product Information Block:'
                            yield '    - MAR channel name: {}'.format(s.channel
                                )
                            yield '    - Product version: {}'.format(s.
                                productversion)
                            yield ''
                        else:
                            yield 'Unknown additional data'
            yield '{:7s} {:7s} {:7s}'.format('SIZE', 'MODE', 'NAME')
            for e in m.mardata.index.entries:
                yield '{:<7d} {:04o}    {}'.format(e.size, e.flags, e.name)