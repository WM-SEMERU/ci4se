def extract_zipped_paths(path):
    if os.path.exists(path):
        return path
    archive, member = os.path.split(path)
    while archive and not os.path.exists(archive):
        archive, prefix = os.path.split(archive)
        member = '/'.join([prefix, member])
    if not zipfile.is_zipfile(archive):
        return path
    zip_file = zipfile.ZipFile(archive)
    if member not in zip_file.namelist():
        return path
    tmp = tempfile.gettempdir()
    extracted_path = os.path.join(tmp, *member.split('/'))
    if not os.path.exists(extracted_path):
        extracted_path = zip_file.extract(member, path=tmp)
    return extracted_path