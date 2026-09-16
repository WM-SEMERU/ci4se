def delete_object(request, model, post_delete_redirect, object_id=None,
    slug=None, slug_field='slug', template_name=None, template_loader=
    loader, extra_context=None, login_required=False, context_processors=
    None, template_object_name='object'):
    if extra_context is None:
        extra_context = {}
    if login_required and not request.user.is_authenticated:
        return redirect_to_login(request.path)
    obj = lookup_object(model, object_id, slug, slug_field)
    if request.method == 'POST':
        obj.delete()
        msg = ugettext('The %(verbose_name)s was deleted.') % {'verbose_name':
            model._meta.verbose_name}
        messages.success(request, msg, fail_silently=True)
        return HttpResponseRedirect(post_delete_redirect)
    else:
        if not template_name:
            template_name = '%s/%s_confirm_delete.html' % (model._meta.
                app_label, model._meta.object_name.lower())
        t = template_loader.get_template(template_name)
        c = {template_object_name: obj}
        apply_extra_context(extra_context, c)
        response = HttpResponse(t.render(context=c, request=request))
        return response