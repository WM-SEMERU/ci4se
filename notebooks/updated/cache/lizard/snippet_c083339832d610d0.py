def _to_ctfile(self):
    output = io.StringIO()
    for entry in self.values():
        output.write(entry['molfile']._to_ctfile())
        for header, values in entry['data'].items():
            output.write('> <{}>\n'.format(header))
            output.write('\n'.join(values))
            output.write('\n')
        output.write('\n$$$$\n')
    return output.getvalue()