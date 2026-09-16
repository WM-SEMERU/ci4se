def export(self, last_checkpoint, output_dir):
    logging.info('Exporting prediction graph to %s', output_dir)
    with tf.Session(graph=tf.Graph()) as sess:
        inputs, outputs = self.build_prediction_graph()
        signature_def_map = {'serving_default': signature_def_utils.
            predict_signature_def(inputs, outputs)}
        init_op = tf.global_variables_initializer()
        sess.run(init_op)
        self.restore_from_checkpoint(sess, self.inception_checkpoint_file,
            last_checkpoint)
        init_op_serving = control_flow_ops.group(variables.
            local_variables_initializer(), tf.tables_initializer())
        builder = saved_model_builder.SavedModelBuilder(output_dir)
        builder.add_meta_graph_and_variables(sess, [tag_constants.SERVING],
            signature_def_map=signature_def_map, legacy_init_op=init_op_serving
            )
        builder.save(False)