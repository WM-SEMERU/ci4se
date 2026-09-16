def scan_download(self, scan_id, format='v2'):
    payload = {'downloadType': format, 'scanResultID': scan_id}
    data = self.raw_query('scanResult', 'download', data=payload, dejson=False)
    bobj = StringIO()
    bobj.write(data)
    zfile = ZipFile(bobj)
    return zfile.read(zfile.namelist()[0])