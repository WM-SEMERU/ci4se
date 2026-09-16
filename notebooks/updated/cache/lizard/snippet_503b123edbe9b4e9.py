def level_matches(self, level, consumer_level):
    if isinstance(level, slice):
        start, stop = level.start, level.stop
        if start is not None and start > consumer_level:
            return False
        if stop is not None and stop <= consumer_level:
            return False
        return True
    else:
        return level >= consumer_level