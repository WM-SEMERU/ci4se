def join_content_version(self, to_cache):
    parts = [self.INTERNAL_VERSION]
    if self.options.versioning:
        parts.append(force_bytes(self.version))
    parts.append(force_bytes(to_cache))
    return self.VERSION_SEPARATOR.join(parts)