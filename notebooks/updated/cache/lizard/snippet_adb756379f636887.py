def compare(orderby_item1, orderby_item2):
    type1_ord = _OrderByHelper.getTypeOrd(orderby_item1)
    type2_ord = _OrderByHelper.getTypeOrd(orderby_item2)
    type_ord_diff = type1_ord - type2_ord
    if type_ord_diff:
        return type_ord_diff
    if type1_ord == 0:
        return 0
    return _compare_helper(orderby_item1['item'], orderby_item2['item'])