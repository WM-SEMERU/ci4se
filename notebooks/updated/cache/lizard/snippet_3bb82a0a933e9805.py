def to_binary_string(self):
    timestamp = datetime_to_timestamp(self.when)
    token = binascii.unhexlify(self.token)
    return struct.pack(self.FORMAT_PREFIX + '{0}s'.format(len(token)),
        timestamp, len(token), token)