def spellcheck(request):
    try:
        raw = request.raw_post_data
        input = json.loads(raw)
        id = input['id']
        method = input['method']
        params = input['params']
        lang = params[0]
        arg = params[1]
        if not enchant.dict_exists(str(lang)):
            raise RuntimeError("dictionary not found for language '%s'" % lang)
        checker = enchant.Dict(str(lang))
        if method == 'checkWords':
            result = [word for word in arg if word and not checker.check(word)]
        elif method == 'getSuggestions':
            result = checker.suggest(arg)
        else:
            raise RuntimeError("Unkown spellcheck method: '%s'" % method)
        output = {'id': id, 'result': result, 'error': None}
    except Exception:
        return HttpResponse('Error running spellchecker')
    return HttpResponse(json.dumps(output), content_type='application/json')