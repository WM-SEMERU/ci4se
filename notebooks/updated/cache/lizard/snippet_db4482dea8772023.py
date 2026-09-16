def export_saved_model(sess, export_dir, tag_set, signatures):
    import tensorflow as tf
    g = sess.graph
    g._unsafe_unfinalize()
    builder = tf.saved_model.builder.SavedModelBuilder(export_dir)
    logging.info('===== signatures: {}'.format(signatures))
    signature_def_map = {}
    for key, sig in signatures.items():
        signature_def_map[key
            ] = tf.saved_model.signature_def_utils.build_signature_def(inputs
            ={name: tf.saved_model.utils.build_tensor_info(tensor) for name,
            tensor in sig['inputs'].items()}, outputs={name: tf.saved_model
            .utils.build_tensor_info(tensor) for name, tensor in sig[
            'outputs'].items()}, method_name=sig['method_name'] if 
            'method_name' in sig else key)
    logging.info('===== signature_def_map: {}'.format(signature_def_map))
    builder.add_meta_graph_and_variables(sess, tag_set.split(','),
        signature_def_map=signature_def_map, clear_devices=True)
    g.finalize()
    builder.save()