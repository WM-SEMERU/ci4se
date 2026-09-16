def fasta_iter(handle, header=None):
    append = list.append
    join = str.join
    strip = str.strip
    next_line = next
    if header is None:
        header = next(handle)
    if isinstance(header, bytes):

        def next_line(i):
            return next(i).decode('utf-8')
        header = strip(header.decode('utf-8'))
    else:
        header = strip(header)
    try:
        while True:
            line = strip(next_line(handle))
            data = FastaEntry()
            try:
                if not header[0] == '>':
                    raise IOError(
                        'Bad FASTA format: no ">" at beginning of line')
            except IndexError:
                raise IOError('Bad FASTA format: file contains blank lines')
            try:
                data.id, data.description = header[1:].split(' ', 1)
            except ValueError:
                data.id = header[1:]
                data.description = ''
            sequence_list = []
            while line and not line[0] == '>':
                append(sequence_list, line)
                line = strip(next_line(handle))
            header = line
            data.sequence = join('', sequence_list)
            yield data
    except StopIteration:
        data.sequence = ''.join(sequence_list)
        yield data