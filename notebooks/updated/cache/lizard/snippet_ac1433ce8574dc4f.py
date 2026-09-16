def decoded_output_boxes(self):
    anchors = tf.tile(tf.expand_dims(self.proposals.boxes, 1), [1, cfg.DATA
        .NUM_CLASS, 1])
    decoded_boxes = decode_bbox_target(self.box_logits / self.
        bbox_regression_weights, anchors)
    return decoded_boxes