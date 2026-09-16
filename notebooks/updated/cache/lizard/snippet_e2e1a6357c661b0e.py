def label_from_instance(self, obj):
    return '%s %s' % (self.level_indicator * getattr(obj, obj._mptt_meta.
        level_attr), obj)