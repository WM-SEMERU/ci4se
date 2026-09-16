def get_next_action(self, request, application, label, roles):
    if label is not None:
        return HttpResponseBadRequest('<h1>Bad Request</h1>')
    actions = self.get_actions(request, application, roles)
    if request.method == 'GET':
        context = self.context
        context.update({'application': application, 'actions': actions,
            'state': self.name, 'roles': roles})
        return render(template_name='kgapplications/common_detail.html',
            context=context, request=request)
    elif request.method == 'POST':
        for action in actions:
            if action in request.POST:
                return action
    return HttpResponseBadRequest('<h1>Bad Request</h1>')