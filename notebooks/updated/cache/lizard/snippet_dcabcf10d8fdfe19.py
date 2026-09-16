def find_references_origin(irs):
    for ir in irs:
        if isinstance(ir, (Index, Member)):
            ir.lvalue.points_to = ir.variable_left