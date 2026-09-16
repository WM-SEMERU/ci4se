def os_details():
    bits, linkage = platform.architecture()
    results = {'platform.arch.bits': bits, 'platform.arch.linkage': linkage,
        'platform.machine': platform.machine(), 'platform.process':
        platform.processor(), 'sys.byteorder': sys.byteorder, 'os.name': os
        .name, 'host.name': socket.gethostname(), 'sys.platform': sys.
        platform, 'platform.system': platform.system(), 'platform.release':
        platform.release(), 'platform.version': platform.version(),
        'encoding.filesystem': sys.getfilesystemencoding()}
    for name in ('sep', 'altsep', 'pathsep', 'linesep'):
        results['os.{0}'.format(name)] = getattr(os, name, None)
    try:
        results['os.cpu_count'] = os.cpu_count()
    except AttributeError:
        results['os.cpu_count'] = None
    try:
        results['sys.dlopenflags'] = sys.getdlopenflags()
    except AttributeError:
        results['sys.dlopenflags'] = None
    return results