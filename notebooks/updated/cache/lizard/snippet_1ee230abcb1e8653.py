def is_backend_enabled(backend):
    if backend == 'onnxruntime':
        try:
            import onnxruntime
            return True
        except ImportError:
            return False
    else:
        raise NotImplementedError("Not implemented for backend '{0}'".
            format(backend))