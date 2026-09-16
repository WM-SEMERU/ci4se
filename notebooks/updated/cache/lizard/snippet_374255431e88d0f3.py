def _load_text_csv_file(self, filename, separator=',', **kwargs):
    rdd_input = self.sc.textFile(filename)

    def load_csv_record(line):
        input_stream = StringIO.StringIO(line)
        reader = csv.reader(input_stream, delimiter=',')
        payload = reader.next()
        key = payload[0]
        rest = payload[1:]
        d = {}
        for cell, i in izip(rest, range(1, 1 + len(rest))):
            d[str(i)] = cell
        d['0'] = key
        return key, d
    rdd_parsed = rdd_input.map(load_csv_record)
    return rdd_parsed