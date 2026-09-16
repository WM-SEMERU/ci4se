def implicit_includes(self, feature, target_type):
    assert isinstance(feature, basestring)
    assert isinstance(target_type, basestring)
    if not target_type:
        key = feature
    else:
        key = feature + '-' + target_type
    result = self.implicit_includes_cache_.get(key)
    if not result:
        target_paths = self.all_target_directories(target_type)
        target_paths = unique(target_paths)
        result = [('<%s>%s' % (feature, p)) for p in target_paths]
        self.implicit_includes_cache_[key] = result
    return result