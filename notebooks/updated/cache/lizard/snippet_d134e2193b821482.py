def _get_list_widget(self, **args):
    widgets = super(CompactCRUDMixin, self)._get_list_widget(**args)
    session_form_widget = self.get_key('session_form_widget', None)
    form_widget = None
    if session_form_widget == 'add':
        form_widget = self._add().get('add')
    elif session_form_widget == 'edit':
        pk = self.get_key('session_form_edit_pk')
        if pk and self.datamodel.get(int(pk)):
            form_widget = self._edit(int(pk)).get('edit')
    return {'list': GroupFormListWidget(list_widget=widgets.get('list'),
        form_widget=form_widget, form_action=self.get_key(
        'session_form_action', ''), form_title=self.get_key(
        'session_form_title', ''))}