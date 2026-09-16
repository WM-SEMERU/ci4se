def _to_gzipfile(self, file_generator):
    with gzip.GzipFile(file_generator.to_path, mode='wb') as outfile:
        for f in file_generator:
            outfile.write(f.writestr(file_generator.to_format).encode())