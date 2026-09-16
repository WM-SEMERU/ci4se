def filter(self, record):
    fmt = LogManager.spec.context_format
    if fmt:
        data = self.context.to_dict()
        if data:
            record.context = fmt % ','.join('%s=%s' % (key, val) for key,
                val in sorted(data.items()) if key and val)
        else:
            record.context = ''
    return True