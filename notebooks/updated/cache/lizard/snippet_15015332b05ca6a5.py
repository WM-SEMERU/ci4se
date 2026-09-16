def create_class(request):
    if request.method == 'GET':
        return render(request, 'classes_create.html', {}, help_text=
            create_class.__doc__)
    if request.method == 'POST':
        if not request.user.is_authenticated() or not hasattr(request.user,
            'userprofile'):
            return render_json(request, {'error': _(
                'User is not logged in.'), 'error_type':
                'user_unauthorized'}, template='classes_create.html',
                status=401)
        data = json_body(request.body.decode('utf-8'))
        if 'code' in data and Class.objects.filter(code=data['code']).exists():
            return render_json(request, {'error': _(
                'A class with this code already exists.'), 'error_type':
                'class_with_code_exists'}, template='classes_create.html',
                status=400)
        if 'name' not in data or not data['name']:
            return render_json(request, {'error': _(
                'Class name is missing.'), 'error_type':
                'missing_class_name'}, template='classes_create.html',
                status=400)
        cls = Class(name=data['name'], owner=request.user.userprofile)
        if 'code' in data:
            cls.code = data['code']
        cls.save()
        return render_json(request, cls.to_json(), template=
            'classes_create.html', status=201)
    else:
        return HttpResponseBadRequest('method %s is not allowed'.format(
            request.method))