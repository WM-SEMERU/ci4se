def writeAnnotation(self, onset_in_seconds, duration_in_seconds,
    description, str_format='utf-8'):
    if str_format == 'utf-8':
        if duration_in_seconds >= 0:
            return write_annotation_utf8(self.handle, np.round(
                onset_in_seconds * 10000).astype(int), np.round(
                duration_in_seconds * 10000).astype(int), du(description))
        else:
            return write_annotation_utf8(self.handle, np.round(
                onset_in_seconds * 10000).astype(int), -1, du(description))
    elif duration_in_seconds >= 0:
        return write_annotation_latin1(self.handle, np.round(
            onset_in_seconds * 10000).astype(int), np.round(
            duration_in_seconds * 10000).astype(int), u(description).encode
            ('latin1'))
    else:
        return write_annotation_latin1(self.handle, np.round(
            onset_in_seconds * 10000).astype(int), -1, u(description).
            encode('latin1'))