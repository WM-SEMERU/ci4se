def create_zip_from_file(zip_file, fname):
    with zipfile.ZipFile(zip_file, 'w') as myzip:
        myzip.write(fname)