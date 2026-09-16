def make_argument_subquery(arg):
    return Subquery.create(arg) if isinstance(arg, (GroupBy, Projection)
        ) or arg.restriction else arg