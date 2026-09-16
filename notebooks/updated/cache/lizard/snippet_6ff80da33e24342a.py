def _data_block(stream):
    while len(stream) > 0:
        line = stream.popleft()
        if line.startswith('>'):
            yield DataHeader(line[1:].strip())
        else:
            data_item = line.strip()
            if data_item:
                yield DataItem(line)
            else:
                continue