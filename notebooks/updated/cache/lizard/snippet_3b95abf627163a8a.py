def write_resultfiles(self):
    t0 = time.time()
    writer = ow.output_writer(output_dictionary=self.result)
    if len(self.options.outpath) >= 3 and self.options.outpath[-3:] == '.h5':
        writer.write_hdf5(filename=self.options.outpath, timestamp=self.
            options.timestamp)
    else:
        writer.write_txt(outdir=self.options.outpath, timestamp=self.
            options.timestamp, delimiter=self.options.delimiter,
            float_format=self.options.float_format)
    t1 = time.time()
    print('Elapsed time for writing the output files is %.2f seconds' % (t1 -
        t0))