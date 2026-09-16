def _get_auto_rank(self, rank):
    if rank == 'auto':
        if self.__class__.__name__ == 'OneCodexAccessor':
            return self._rank
        if self._field == 'abundance':
            return 'species'
        else:
            return 'genus'
    else:
        return rank