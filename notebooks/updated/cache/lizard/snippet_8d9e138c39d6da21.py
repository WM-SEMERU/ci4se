def load(self, text, lineterminator='\r\n', quotechar='"', delimiter=',',
    escapechar=escapechar, quoting=csv.QUOTE_MINIMAL):
    f = io.StringIO(text)
    if not quotechar:
        quoting = csv.QUOTE_NONE
    reader = csv.DictReader(f, delimiter=delimiter, quotechar=quotechar,
        quoting=quoting, lineterminator=lineterminator)
    if reader.fieldnames:
        reader.fieldnames = [field.strip() for field in reader.fieldnames]
    try:
        self.primitive = next(reader)
    except StopIteration:
        self.primitive = {}