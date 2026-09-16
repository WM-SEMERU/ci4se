def save(self, *args, **kwargs):
    from tracked_model.models import History, RequestInfo
    if self.pk:
        action = ActionType.UPDATE
        changes = None
    else:
        action = ActionType.CREATE
        changes = serializer.dump_model(self)
    request = kwargs.pop('request', None)
    track_token = kwargs.pop('track_token', None)
    super().save(*args, **kwargs)
    if not changes:
        changes = self._tracked_model_diff()
    if changes:
        hist = History()
        hist.model_name = self._meta.model.__name__
        hist.app_label = self._meta.app_label
        hist.table_name = self._meta.db_table
        hist.table_id = self.pk
        hist.change_log = serializer.to_json(changes)
        hist.action_type = action
        if request:
            if request.user.is_authenticated():
                hist.revision_author = request.user
            req_info = RequestInfo.create_or_get_from_request(request)
            hist.revision_request = req_info
        elif track_token:
            hist.revision_author_id = track_token.user_pk
            hist.revision_request_id = track_token.request_pk
        hist.save()
    self._tracked_model_initial_state = serializer.dump_model(self)