def maybe_cythonize(extensions, *args, **kwargs):
    if len(sys.argv) > 1 and 'clean' in sys.argv:
        return extensions
    if not cython:
        return extensions
    numpy_incl = pkg_resources.resource_filename('numpy', 'core/include')
    for ext in extensions:
        if hasattr(ext, 'include_dirs') and numpy_incl not in ext.include_dirs:
            ext.include_dirs.append(numpy_incl)
    build_ext.render_templates(_pxifiles)
    return cythonize(extensions, *args, **kwargs)