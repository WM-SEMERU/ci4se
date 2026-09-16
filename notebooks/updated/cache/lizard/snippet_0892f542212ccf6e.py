def category(self):
    if self.id in ('reg', 'mem'):
        return self.id
    elif self._abstract_backer:
        return 'mem'
    elif self.id.startswith('file'):
        return 'file'
    else:
        raise SimMemoryError(
            'Unknown SimMemory category for memory_id "%s"' % self.id)