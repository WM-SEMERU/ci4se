def minimize(self, model, session=None, var_list=None, feed_dict=None,
    maxiter=1000, disp=False, initialize=False, anchor=True, step_callback=
    None, **kwargs):
    if model is None or not isinstance(model, Model):
        raise ValueError('Unknown type passed for optimization.')
    if model.is_built_coherence() is Build.NO:
        raise GPflowError('Model is not built.')
    session = model.enquire_session(session)
    self._model = model
    optimizer = self.make_optimize_tensor(model, session, var_list=var_list,
        maxiter=maxiter, disp=disp)
    self._optimizer = optimizer
    feed_dict = self._gen_feed_dict(model, feed_dict)
    optimizer.minimize(session=session, feed_dict=feed_dict, step_callback=
        step_callback, **kwargs)
    if anchor:
        model.anchor(session)