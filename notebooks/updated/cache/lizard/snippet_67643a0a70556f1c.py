def save_model(self, request, obj, form, change):
    obj._history_user = request.user
    super(SimpleHistoryAdmin, self).save_model(request, obj, form, change)