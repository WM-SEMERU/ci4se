def no_instance_caching():
    orig_flag = Expression.instance_caching
    Expression.instance_caching = False
    try:
        yield
    finally:
        Expression.instance_caching = orig_flag