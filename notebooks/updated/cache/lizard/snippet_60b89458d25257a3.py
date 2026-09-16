def _do_auto_predict(machine, X, *args):
    if auto_predict and hasattr(machine, 'predict'):
        return machine.predict(X)