def order_to_dict(order):
    default = Order()
    return {field: val for field, val in vars(order).items() if val !=
        getattr(default, field, None)}