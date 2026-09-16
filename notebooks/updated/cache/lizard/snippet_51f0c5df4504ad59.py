def sg_restore(sess, save_path, category=''):
    r
    if not isinstance(category, (tuple, list)):
        category = [category]
    var_list = {}
    for cat in category:
        for t in tf.global_variables():
            if t.name.startswith(cat):
                var_list[t.name[:-2]] = t
    saver = tf.train.Saver(var_list)
    saver.restore(sess, save_path)