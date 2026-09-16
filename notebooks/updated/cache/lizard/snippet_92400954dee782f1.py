def convert_base(arg, from_base, to_base):
    return ops.BaseConvert(arg, from_base, to_base).to_expr()