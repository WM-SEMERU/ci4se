def select_site_view(self, request, form_url=''):
    if not self.has_add_permission(request):
        raise PermissionDenied
    extra_qs = ''
    if request.META['QUERY_STRING']:
        extra_qs = '&' + request.META['QUERY_STRING']
    site_choices = self.get_site_choices()
    if len(site_choices) == 1:
        return HttpResponseRedirect('?site_id={0}{1}'.format(site_choices[0
            ][0], extra_qs))
    form = self.select_site_form(data=request.POST if request.method ==
        'POST' else None, initial={'site': site_choices[0][0]})
    form.fields['site'].choices = site_choices
    if form.is_valid():
        return HttpResponseRedirect('?site_id={0}{1}'.format(form.
            cleaned_data['site'], extra_qs))
    fieldsets = (None, {'fields': ('site',)}),
    adminForm = AdminForm(form, fieldsets, {}, model_admin=self)
    media = self.media + adminForm.media
    context = {'title': _('Add %s') % force_text(self.opts.verbose_name),
        'adminform': adminForm, 'is_popup': '_popup' in request.GET,
        'media': mark_safe(media), 'errors': AdminErrorList(form, ()),
        'app_label': self.opts.app_label}
    return self.render_select_site_form(request, context, form_url)