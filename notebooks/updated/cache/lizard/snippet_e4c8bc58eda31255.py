def _stdlib_paths():
    attr_candidates = ['prefix', 'real_prefix', 'base_prefix']
    prefixes = (getattr(sys, a) for a in attr_candidates if hasattr(sys, a))
    version = 'python%s.%s' % sys.version_info[0:2]
    return set(os.path.abspath(os.path.join(p, 'lib', version)) for p in
        prefixes)