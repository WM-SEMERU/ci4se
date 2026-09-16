def get_list_display(self, request):
    list_display = list(super(VersionedAdmin, self).get_list_display(request))
    if self.list_display_show_identity:
        list_display = ['identity_shortener'] + list_display
    if self.list_display_show_start_date:
        list_display += ['version_start_date']
    if self.list_display_show_end_date:
        list_display += ['version_end_date']
    return list_display + ['is_current']