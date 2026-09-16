def _read_table(self, filename):
    filename = pkg_resources.resource_filename(__name__, filename)
    segments = []
    with open(filename, 'rb') as f:
        reader = csv.reader(f, encoding='utf-8')
        header = next(reader)
        names = header[1:]
        for row in reader:
            seg = row[0]
            vals = row[1:]
            specs = set(zip(vals, names))
            segments.append((seg, specs))
    seg_dict = dict(segments)
    return segments, seg_dict, names