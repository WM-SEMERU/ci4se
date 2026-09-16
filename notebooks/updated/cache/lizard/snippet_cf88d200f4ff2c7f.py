def compute_gzip_md5(file_name):
    md5 = hashlib.md5()
    file_obj = gzip.open(file_name, 'rb')
    for chunk in iter(lambda : file_obj.read(8192), ''):
        md5.update(chunk)
    file_obj.close()
    return md5.hexdigest()