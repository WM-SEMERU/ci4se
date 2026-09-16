def reader(self, fp, encoding):
    _, suffix = os.path.splitext(fp.name)
    if suffix == '.gz':
        fp.close()
        return gzip.open(fp.name)
    elif suffix == '.json':
        return json.load(fp)
    elif suffix == '.csv' or self.delimiter:
        return csvreader(fp, encoding, delimiter=self.delimiter or ',')
    elif suffix == '.tsv':
        return csvreader(fp, encoding, delimiter='\t')
    return fp