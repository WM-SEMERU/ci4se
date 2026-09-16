def action_is_satisfied(action):
    num_consumed_args = getattr(action, 'num_consumed_args', 0)
    if action.nargs == ONE_OR_MORE and num_consumed_args < 1:
        return False
    else:
        if action.nargs is None:
            action.nargs = 1
        try:
            return num_consumed_args == action.nargs
        except:
            return True