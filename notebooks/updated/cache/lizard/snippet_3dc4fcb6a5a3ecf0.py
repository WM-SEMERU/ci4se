def wrap_objective(f, *args, **kwds):
    objective_func = f(*args, **kwds)
    objective_name = f.__name__
    args_str = ' [' + ', '.join([_make_arg_str(arg) for arg in args]) + ']'
    description = objective_name.title() + args_str
    return Objective(objective_func, objective_name, description)