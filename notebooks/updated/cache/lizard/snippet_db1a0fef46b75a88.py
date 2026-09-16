def _get_hash_object(hash_algo_name):
    algorithms = (hashlib.algorithms_guaranteed if six.PY3 else hashlib.
        algorithms)
    if hash_algo_name not in algorithms:
        msg = "Unsupported/Invalid hash name '%s' provided." % hash_algo_name
        raise exception.InvalidInputError(msg)
    return getattr(hashlib, hash_algo_name)()