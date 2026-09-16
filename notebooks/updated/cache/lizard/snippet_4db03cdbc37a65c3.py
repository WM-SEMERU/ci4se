def do_first(self):
    pid = os.getpid()
    self.basename = os.path.join(self.tmpdir, 'iiif_netpbm_' + str(pid))
    outfile = self.basename + '.pnm'
    filetype = self.file_type(self.srcfile)
    if filetype == 'png':
        if self.shell_call(self.pngtopnm + ' ' + self.srcfile + ' > ' + outfile
            ):
            raise IIIFError(text='Oops... got error from pngtopnm.')
    elif filetype == 'jpg':
        if self.shell_call(self.jpegtopnm + ' ' + self.srcfile + ' > ' +
            outfile):
            raise IIIFError(text='Oops... got error from jpegtopnm.')
    else:
        raise IIIFError(code='501', text=
            'bad input file format (only know how to read png/jpeg)')
    self.tmpfile = outfile
    self.width, self.height = self.image_size(self.tmpfile)