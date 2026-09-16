def _check_algorithm_keys(item):
    problem_keys = [k for k in item['algorithm'].keys() if k not in
        ALGORITHM_KEYS]
    if len(problem_keys) > 0:
        raise ValueError(
            """Unexpected configuration keyword in 'algorithm' section: %s
See configuration documentation for supported options:
%s
"""
             % (problem_keys, ALG_DOC_URL))