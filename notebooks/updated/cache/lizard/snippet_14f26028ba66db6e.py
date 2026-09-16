def flat_map(self, flatmap_fn):
    op = Operator(_generate_uuid(), OpType.FlatMap, 'FlatMap', flatmap_fn,
        num_instances=self.env.config.parallelism)
    return self.__register(op)