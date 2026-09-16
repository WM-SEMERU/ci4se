def check_signing_file(self, keyid, signing_file):
    if not signing_file or not os.path.exists(signing_file):
        return False
    if not self.check_permissions(signing_file):
        log.warning('Wrong permissions for %s, ignoring content', signing_file)
        return False
    mtime = os.path.getmtime(signing_file)
    if self.signing_files.get(signing_file, {}).get('mtime') != mtime:
        self.signing_files.setdefault(signing_file, {})['mtime'] = mtime
        with salt.utils.files.fopen(signing_file, 'r') as fp_:
            self.signing_files[signing_file]['data'] = [entry for entry in
                [line.strip() for line in fp_] if not entry.strip().
                startswith('#')]
    return any(salt.utils.stringutils.expr_match(keyid, line) for line in
        self.signing_files[signing_file].get('data', []))