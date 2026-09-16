def create_module_spec(module_fn, tags_and_args=None, drop_collections=None):
    if not drop_collections:
        drop_collections = []
    report_tags = True
    if not tags_and_args:
        tags_and_args = [(set(), {})]
        report_tags = False
    saved_model_handler = saved_model_lib.SavedModelHandler()
    for tags, args in tags_and_args:
        with tf.Graph().as_default() as graph:
            with tf_v1.variable_scope('', use_resource=True):
                module_fn(**args)
            for collection_key in drop_collections:
                del tf_v1.get_collection_ref(collection_key)[:]
        err = find_state_op_colocation_error(graph, tags if report_tags else
            None)
        if err:
            raise ValueError(err)
        saved_model_handler.add_graph_copy(graph, tags=tags)
    return _ModuleSpec(saved_model_handler, checkpoint_variables_path=None)