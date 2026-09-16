def get_args(self, state, is_fp=None, sizes=None, stack_base=None):
    if sizes is None and self.func_ty is not None:
        sizes = [arg.size for arg in self.func_ty.args]
    if is_fp is None:
        if self.args is None:
            if self.func_ty is None:
                raise ValueError(
                    'You must either customize this CC or pass a value to is_fp!'
                    )
            else:
                arg_locs = self.arg_locs([False] * len(self.func_ty.args))
        else:
            arg_locs = self.args
    elif type(is_fp) is int:
        if self.args is not None and len(self.args) != is_fp:
            raise ValueError(
                'Bad number of args requested: got %d, expected %d' % (
                is_fp, len(self.args)))
        arg_locs = self.arg_locs([False] * is_fp, sizes)
    else:
        arg_locs = self.arg_locs(is_fp, sizes)
    return [loc.get_value(state, stack_base=stack_base) for loc in arg_locs]