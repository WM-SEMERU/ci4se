def get_instance(jar_filename=None, version=None, download_if_missing=True,
    backend='jpype', **extra_args):
    StanfordDependencies._raise_on_bad_jar_filename(jar_filename)
    extra_args.update(jar_filename=jar_filename, download_if_missing=
        download_if_missing, version=version)
    if backend == 'jpype':
        try:
            from .JPypeBackend import JPypeBackend
            return JPypeBackend(**extra_args)
        except ImportError:
            warnings.warn(
                'Error importing JPypeBackend, falling back to SubprocessBackend.'
                )
            backend = 'subprocess'
        except RuntimeError as r:
            warnings.warn(
                'RuntimeError with JPypeBackend (%s), falling back to SubprocessBackend.'
                 % r[0])
            backend = 'subprocess'
        except TypeError as t:
            warnings.warn(
                'TypeError with JPypeBackend (%s), falling back to SubprocessBackend.'
                 % t[0])
            backend = 'subprocess'
    if backend == 'subprocess':
        from .SubprocessBackend import SubprocessBackend
        return SubprocessBackend(**extra_args)
    raise ValueError(
        "Unknown backend: %r (known backends: 'subprocess' and 'jpype')" %
        backend)