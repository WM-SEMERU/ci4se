def editpermissions_group_view(self, request, group_id, forum_id=None):
    group = get_object_or_404(Group, pk=group_id)
    forum = get_object_or_404(Forum, pk=forum_id) if forum_id else None
    context = self.get_forum_perms_base_context(request, forum)
    context['forum'] = forum
    context['title'] = '{} - {}'.format(_('Forum permissions'), group)
    context['form'] = self._get_permissions_form(request,
        GroupForumPermission, {'forum': forum, 'group': group})
    return render(request, self.editpermissions_group_view_template_name,
        context)