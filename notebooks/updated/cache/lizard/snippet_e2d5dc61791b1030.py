def for_new_graph(*args, **kwargs):
    graph = tf.Graph()
    with graph.as_default():
        return for_default_graph(*args, **kwargs)