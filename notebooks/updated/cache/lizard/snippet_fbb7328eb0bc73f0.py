def check_between(v_min, v_max, **params):
    for p in params:
        if params[p] < v_min or params[p] > v_max:
            raise ValueError('Expected {} between {} and {}, got {}'.format
                (p, v_min, v_max, params[p]))