def check_postconditions(f, return_value):
    f = getattr(f, 'wrapped_fn', f)
    if f and hasattr(f, 'postconditions'):
        for cond in f.postconditions:
            cond(return_value)