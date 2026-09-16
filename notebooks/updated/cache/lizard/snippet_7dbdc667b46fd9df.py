def get_num_processors():
    try:
        return os.cpu_count()
    except AttributeError:
        pass
    try:
        import multiprocessing
        return multiprocessing.cpu_count()
    except ImportError:
        pass
    except NotImplementedError:
        pass
    try:
        from subprocess32 import check_output
        ncpus = check_output('nproc')
        return int(ncpus)
    except CalledProcessError:
        pass
    except (ValueError, TypeError):
        pass
    except ImportError:
        pass
    try:
        from subprocess import check_output
        ncpus = check_output('nproc')
        return int(ncpus)
    except CalledProcessError:
        pass
    except (ValueError, TypeError):
        pass
    except ImportError:
        pass
    raise RuntimeError('Cannot determine number of processors')