def c_delete(api, args, verbose=False):
    obj = api.get_object(args['<URL>'].split('/')[-1])
    obj.delete()
    if verbose:
        return ['deleted object at', api.url(obj)]