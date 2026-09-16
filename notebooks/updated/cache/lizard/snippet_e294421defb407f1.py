def get_return_val(self, state, is_fp=None, size=None, stack_base=None):
    ty = self.func_ty.returnty if self.func_ty is not None else None
    if self.ret_val is not None:
        loc = self.ret_val
    elif is_fp is not None:
        loc = self.FP_RETURN_VAL if is_fp else self.RETURN_VAL
    elif ty is not None:
        loc = self.FP_RETURN_VAL if isinstance(ty, SimTypeFloat
            ) else self.RETURN_VAL
    else:
        loc = self.RETURN_VAL
    if loc is None:
        raise NotImplementedError(
            "This SimCC doesn't know how to get this value - should be implemented"
            )
    val = loc.get_value(state, stack_base=stack_base, size=None if ty is
        None else ty.size // state.arch.byte_width)
    if self.is_fp_arg(loc) or self.is_fp_value(val) or isinstance(ty,
        SimTypeFloat):
        val = val.raw_to_fp()
    return val