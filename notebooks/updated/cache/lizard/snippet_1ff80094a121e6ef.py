def build_prediction_graph(self):
    tensors = self.build_graph(None, 1, GraphMod.PREDICT)
    keys_placeholder = tf.placeholder(tf.string, shape=[None])
    inputs = {'key': keys_placeholder, 'image_bytes': tensors.input_jpeg}
    keys = tf.identity(keys_placeholder)
    labels = self.labels + ['UNKNOWN']
    labels_tensor = tf.constant(labels)
    labels_table = tf.contrib.lookup.index_to_string_table_from_tensor(mapping
        =labels_tensor)
    predicted_label = labels_table.lookup(tensors.predictions[0])
    labels_tensor = tf.expand_dims(tf.constant(labels), 0)
    num_instance = tf.shape(keys)
    labels_tensors_n = tf.tile(labels_tensor, tf.concat(axis=0, values=[
        num_instance, [1]]))
    outputs = {'key': keys, 'prediction': predicted_label, 'labels':
        labels_tensors_n, 'scores': tensors.predictions[1]}
    return inputs, outputs