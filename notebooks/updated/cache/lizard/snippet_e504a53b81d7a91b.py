def restore(self, request, *args, **kwargs):
    paths = request.path_info.split('/')
    object_id_index = paths.index('restore') - 2
    object_id = paths[object_id_index]
    obj = super(VersionedAdmin, self).get_object(request, object_id)
    obj.restore()
    admin_wordIndex = object_id_index - 3
    path = '/%s' % '/'.join(paths[admin_wordIndex:object_id_index])
    opts = self.model._meta
    msg_dict = {'name': force_text(opts.verbose_name), 'obj': format_html(
        '<a href="{}">{}</a>', urlquote(request.path), obj)}
    msg = format_html(_('The {name} "{obj}" was restored successfully.'),
        **msg_dict)
    self.message_user(request, msg, messages.SUCCESS)
    return HttpResponseRedirect(path)