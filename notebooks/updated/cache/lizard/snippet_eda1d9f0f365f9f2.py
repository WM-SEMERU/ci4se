def joint_value_post_processor(a, _):
    if len(a) == 1:
        return a[0]
    product = 1
    for v in a:
        new_value = 1 - v
        product = product * new_value
    joint_value = 1 - product
    return joint_value