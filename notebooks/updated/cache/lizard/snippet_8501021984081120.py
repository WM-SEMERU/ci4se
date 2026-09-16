def build(format='qcow2', path='/tmp/'):
    try:
        _('collector').Inspector(cachedir=__opts__['cachedir'], piddir=os.
            path.dirname(__opts__['pidfile']), pidfilename='').reuse_snapshot(
            ).build(format=format, path=path)
    except InspectorKiwiProcessorException as ex:
        raise CommandExecutionError(ex)
    except Exception as ex:
        log.error(_get_error_message(ex))
        raise Exception(ex)