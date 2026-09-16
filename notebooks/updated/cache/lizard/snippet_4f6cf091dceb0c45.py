def add(self, filename, raw_data=None, dx=None):
    if not raw_data:
        log.debug("Loading file from '{}'".format(filename))
        with open(filename, 'rb') as fp:
            raw_data = fp.read()
    ret = androconf.is_android_raw(raw_data)
    log.debug("Found filetype: '{}'".format(ret))
    if not ret:
        return None
    if ret == 'APK':
        digest, _ = self.addAPK(filename, raw_data)
    elif ret == 'DEX':
        digest, _, _ = self.addDEX(filename, raw_data, dx)
    elif ret == 'DEY':
        digest, _, _ = self.addDEY(filename, raw_data, dx)
    else:
        return None
    return digest