def dump_session_params(path):
    var = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES)
    var.extend(tf.get_collection(tf.GraphKeys.MODEL_VARIABLES))
    assert len(set(var)) == len(var
        ), 'TRAINABLE and MODEL variables have duplication!'
    gvars = set([k.name for k in tf.global_variables()])
    var = [v for v in var if v.name in gvars]
    result = {}
    for v in var:
        result[v.name] = v.eval()
    save_chkpt_vars(result, path)