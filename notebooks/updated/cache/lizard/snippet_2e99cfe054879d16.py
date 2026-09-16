def post(request):
    data = request.POST or json.loads(request.body)['body']
    key = data.get('key', None)
    val = data.get('val', None)
    res = Result()
    if key is not None and val is not None:
        obj, created = UserPref.objects.get_or_create(user=request.user)
        if created:
            obj.data = json.dumps(DefaultPrefs.copy())
            obj.save()
        try:
            val = json.loads(val)
        except (TypeError, ValueError):
            pass
        obj.setKey(key, val)
        obj.save()
        res.append(obj.json())
    return JsonResponse(res.asDict())