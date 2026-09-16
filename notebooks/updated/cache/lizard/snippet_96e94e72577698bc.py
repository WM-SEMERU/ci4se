def multilevel_rpn_losses(multilevel_anchors, multilevel_label_logits,
    multilevel_box_logits):
    num_lvl = len(cfg.FPN.ANCHOR_STRIDES)
    assert len(multilevel_anchors) == num_lvl
    assert len(multilevel_label_logits) == num_lvl
    assert len(multilevel_box_logits) == num_lvl
    losses = []
    with tf.name_scope('rpn_losses'):
        for lvl in range(num_lvl):
            anchors = multilevel_anchors[lvl]
            label_loss, box_loss = rpn_losses(anchors.gt_labels, anchors.
                encoded_gt_boxes(), multilevel_label_logits[lvl],
                multilevel_box_logits[lvl], name_scope='level{}'.format(lvl +
                2))
            losses.extend([label_loss, box_loss])
        total_label_loss = tf.add_n(losses[::2], name='label_loss')
        total_box_loss = tf.add_n(losses[1::2], name='box_loss')
        add_moving_summary(total_label_loss, total_box_loss)
    return [total_label_loss, total_box_loss]