def _set_grouper(self, obj, sort=False):
    if self.key is not None and self.level is not None:
        raise ValueError('The Grouper cannot specify both a key and a level!')
    if self._grouper is None:
        self._grouper = self.grouper
    if self.key is not None:
        key = self.key
        if getattr(self.grouper, 'name', None) == key and isinstance(obj,
            ABCSeries):
            ax = self._grouper.take(obj.index)
        else:
            if key not in obj._info_axis:
                raise KeyError('The grouper name {0} is not found'.format(key))
            ax = Index(obj[key], name=key)
    else:
        ax = obj._get_axis(self.axis)
        if self.level is not None:
            level = self.level
            if isinstance(ax, MultiIndex):
                level = ax._get_level_number(level)
                ax = Index(ax._get_level_values(level), name=ax.names[level])
            elif level not in (0, ax.name):
                raise ValueError('The level {0} is not valid'.format(level))
    if (self.sort or sort) and not ax.is_monotonic:
        indexer = self.indexer = ax.argsort(kind='mergesort')
        ax = ax.take(indexer)
        obj = obj._take(indexer, axis=self.axis, is_copy=False)
    self.obj = obj
    self.grouper = ax
    return self.grouper