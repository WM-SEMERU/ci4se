def remove_prefix(self, id):
    if 'prefix' not in request.params:
        abort(400, 'Missing prefix.')
    prefix = Prefix.get(int(request.params['prefix']))
    prefix.pool = None
    prefix.save()
    redirect(url(controller='pool', action='edit', id=id))