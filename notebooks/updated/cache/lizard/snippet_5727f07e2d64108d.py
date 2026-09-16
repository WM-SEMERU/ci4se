def unpack_grad_tuple(gv, gpt):
    elt_widths = [x.num_elements() for x in gpt.shapes]
    with tf.device(gv[0][0].device):
        with tf.name_scope('unpack'):
            splits = tf.split(gv[0], elt_widths)
            unpacked_gv = []
            for idx, s in enumerate(splits):
                unpacked_gv.append((tf.reshape(s, gpt.shapes[idx]), gpt.
                    vars[idx]))
    return unpacked_gv