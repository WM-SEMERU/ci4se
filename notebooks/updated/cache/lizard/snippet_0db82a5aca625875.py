def process_value(self, value):
    if api.is_uid(value):
        return self.to_super_model(value)
    elif api.is_object(value):
        return self.to_super_model(value)
    elif isinstance(value, basestring):
        return safe_unicode(value).encode('utf-8')
    elif isinstance(value, DateTime):
        return value
    elif isinstance(value, (LazyMap, list, tuple)):
        return map(self.process_value, value)
    elif isinstance(value, dict):
        return {k: self.process_value(v) for k, v in value.iteritems()}
    elif safe_callable(value):
        return self.process_value(value())
    return value