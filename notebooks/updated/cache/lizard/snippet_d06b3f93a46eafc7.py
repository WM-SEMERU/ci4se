def get_vars(self):
    try:
        if tf.executing_eagerly():
            raise NotImplementedError(
                'For Eager execution - get_vars must be overridden.')
    except AttributeError:
        pass
    done = False
    tried_to_make_params = False
    while not done:
        trainable_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES,
            self.scope + '/')
        model_vars = tf.get_collection(tf.GraphKeys.MODEL_VARIABLES, self.
            scope + '/')
        scope_vars = ordered_union(trainable_vars, model_vars)
        if len(scope_vars) > 0:
            done = True
        else:
            assert not tried_to_make_params
            tried_to_make_params = True
            self.make_params()
    if hasattr(self, 'num_vars'):
        assert self.num_vars == len(scope_vars)
    else:
        self.num_vars = len(scope_vars)
    return scope_vars