def restore_state(output_dir):
    params_file = os.path.join(output_dir, 'model.pkl')
    if not gfile.exists(params_file):
        return State(step=None, params=None, history=trax_history.History())
    with gfile.GFile(params_file, 'rb') as f:
        params, step, history = pickle.load(f)
    log('Model loaded from %s at step %d' % (params_file, step))
    logging.debug('From loaded model : history = %s', history)
    return State(step=step, params=params, history=history)