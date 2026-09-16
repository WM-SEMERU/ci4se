def times(filenames, tolerance=2):
    times = {}
    delta = datetime.timedelta(seconds=tolerance)
    if isinstance(filenames, str):
        filenames = [filenames]
    for filename in filenames:
        with open(filename, 'r') as stream:
            times[filename] = list()
            header, packet = stream.read()
            start, stop = header.timestamp, header.timestamp
            for header, packet in stream:
                if header.timestamp - stop > delta:
                    times[filename].append((start, stop))
                    start = header.timestamp
                stop = header.timestamp
            times[filename].append((start, stop))
    return times