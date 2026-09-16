def infuse_metadata(graph_def, info):
    temp_graph = tf.Graph()
    with temp_graph.as_default():
        tf.constant(json.dumps(info, cls=NumpyJSONEncoder), name=
            metadata_node_name)
    meta_node = temp_graph.as_graph_def().node[0]
    graph_def.node.extend([meta_node])