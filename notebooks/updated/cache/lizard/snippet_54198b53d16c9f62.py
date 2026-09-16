def get_params(self):
    if hasattr(self, 'params'):
        return list(self.params)
    try:
        if tf.executing_eagerly():
            raise NotImplementedError(
                'For Eager execution - get_params must be overridden.')
    except AttributeError:
        pass
    scope_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, self.
        scope + '/')
    if len(scope_vars) == 0:
        self.make_params()
        scope_vars = tf.get_collection(tf.GraphKeys.TRAINABLE_VARIABLES, 
            self.scope + '/')
        assert len(scope_vars) > 0
    if hasattr(self, 'num_params'):
        if self.num_params != len(scope_vars):
            print('Scope: ', self.scope)
            print('Expected ' + str(self.num_params) + ' variables')
            print('Got ' + str(len(scope_vars)))
            for var in scope_vars:
                print('\t' + str(var))
            assert False
    else:
        self.num_params = len(scope_vars)
    return scope_vars