def replace_header(self, header_text):
    with open(self.outfile, 'rt') as fp:
        _, body = self.split_header(fp)
    with open(self.outfile, 'wt') as fp:
        fp.write(header_text)
        fp.writelines(body)