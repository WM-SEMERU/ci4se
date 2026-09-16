def save(self, filething=None, v2_version=4, v23_sep='/', padding=None):
    fileobj = filething.fileobj
    fileobj.seek(0)
    dsd_header = DSDChunk(fileobj)
    if dsd_header.offset_metdata_chunk == 0:
        fileobj.seek(0, 2)
        dsd_header.offset_metdata_chunk = fileobj.tell()
        dsd_header.write()
    try:
        data = self._prepare_data(fileobj, dsd_header.offset_metdata_chunk,
            self.size, v2_version, v23_sep, padding)
    except ID3Error as e:
        reraise(error, e, sys.exc_info()[2])
    fileobj.seek(dsd_header.offset_metdata_chunk)
    fileobj.write(data)
    fileobj.truncate()
    dsd_header.total_size = fileobj.tell()
    dsd_header.write()