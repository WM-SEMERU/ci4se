def determine_emitter(cls, request):
    default_emitter = cls._meta.emitters[0]
    if not request:
        return default_emitter
    if request.method == 'OPTIONS':
        return JSONEmitter
    accept = request.META.get('HTTP_ACCEPT', '*/*')
    if accept == '*/*':
        return default_emitter
    base_format = mimeparse.best_match(cls._meta.emitters_dict.keys(), accept)
    return cls._meta.emitters_dict.get(base_format, default_emitter)