def get_hash(self, length=HASH_LENGTH):
    data_hash = ''
    if not self.data_str:
        return data_hash
    encoded_data_str = self.data_str
    if sys.version_info.major == 2:
        if isinstance(self.data_str, unicode):
            encoded_data_str = self.data_str.encode('utf-8')
    else:
        encoded_data_str = self.data_str.encode('utf-8')
    data_hash = hashlib.sha1(encoded_data_str).hexdigest()
    return data_hash[:length]