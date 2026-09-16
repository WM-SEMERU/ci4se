def compare(self, path, prefixed_path, source_storage):
    comparitor = getattr(self, 'compare_%s' % self.comparison_method, None)
    if not comparitor:
        comparitor = self._create_comparitor(self.comparison_method)
    return comparitor(path, prefixed_path, source_storage)