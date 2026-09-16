def fill(self, data, dialect):
    csvfile = cStringIO.StringIO()
    csvwriter = csv.writer(csvfile, dialect=dialect)
    for i, line in enumerate(data):
        csvwriter.writerow(list(encode_gen(line)))
        if i >= self.preview_lines:
            break
    preview = csvfile.getvalue()
    csvfile.close()
    preview = preview.decode('utf-8').replace('\r\n', '\n')
    self.SetValue(preview)