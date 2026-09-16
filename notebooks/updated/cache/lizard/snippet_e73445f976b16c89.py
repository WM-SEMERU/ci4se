def enable_death_signal(_warn=True):
    if platform.system() != 'Linux':
        return
    try:
        import prctl
    except ImportError:
        if _warn:
            log_once(
                '"import prctl" failed! Install python-prctl so that processes can be cleaned with guarantee.'
                , 'warn')
        return
    else:
        assert hasattr(prctl, 'set_pdeathsig'
            ), "prctl.set_pdeathsig does not exist! Note that you need to install 'python-prctl' instead of 'prctl'."
        prctl.set_pdeathsig(signal.SIGHUP)