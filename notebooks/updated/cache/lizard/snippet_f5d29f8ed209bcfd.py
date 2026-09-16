def underlying_variable(t):
    t = underlying_variable_ref(t)
    assert t is not None
    if not hasattr(tf.get_default_graph(), 'var_index'):
        tf.get_default_graph().var_index = {}
    var_index = tf.get_default_graph().var_index
    for v in tf.global_variables()[len(var_index):]:
        var_index[v.name] = v
    return var_index[t.name]