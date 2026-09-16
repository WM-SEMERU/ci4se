def AbortProcessing(obj, eng, callbacks, exc_info):
    msg = 'Processing was aborted for object: {0}'.format(obj.id)
    eng.log.debug(msg)
    raise Break