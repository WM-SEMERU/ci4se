def zadd(self, name, *args, **kwargs):
    pieces = []
    if args:
        if len(args) % 2 != 0:
            raise ValueError(
                'ZADD requires an equal number of values and scores')
        pieces.extend(args)
    for pair in kwargs.items():
        pieces.append(pair[1])
        pieces.append(pair[0])
    return self.execute_command('ZADD', name, *pieces)