def load_classifiers(algo_defs, env):
    if not isinstance(algo_defs, Iterable):
        algo_defs = [algo_defs]
    load_algorithms(algo_defs, 'BaseTrainingAlgorithm', env)