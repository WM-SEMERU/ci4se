def _guess(self, filename):
    encoding = None
    file_size = os.path.getsize(filename)
    if not self._is_very_large(file_size):
        with open(filename, 'rb') as f:
            if file_size == 0:
                encoding = 'ascii'
            else:
                encoding = self._detect_buffer_encoding(f)
                if encoding is None:
                    raise UnicodeDecodeError('None', b'', 0, 0,
                        'Unicode cannot be detected.')
                if encoding != BINARY_ENCODE:
                    encoding = self._verify_encoding(encoding)
    else:
        raise UnicodeDecodeError('None', b'', 0, 0,
            'Unicode detection is not applied to very large files!')
    return encoding