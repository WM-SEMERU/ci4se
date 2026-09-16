def write_txt(self, as_string=False):
    if not as_string:
        with open('{}/{}.txt'.format(self.outpath, self.outputprefix), 'w'
            ) as f:
            [f.write(textline + '\n') for textline in self.txtreport]
    else:
        output = '\n'.join(self.txtreport)
        if config.RAWSTRING:
            output = repr(output)
        print(output)