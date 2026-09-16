def update_stampfile_hook(self, dependencies):
    hashes = {d: _sha1_for_file(d) for d in dependencies if os.path.exists(d)}
    with open(self._stamp_file_hashes_path, 'wb') as hashes_file:
        hashes_file.write(json.dumps(hashes).encode('utf-8'))