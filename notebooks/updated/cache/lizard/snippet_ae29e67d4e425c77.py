def notify_state_name_change(self, model, prop_name, info):
    if is_execution_status_update_notification_from_state_machine_model(
        prop_name, info):
        return
    overview = NotificationOverview(info, False, self.__class__.__name__)
    changed_model = overview['model'][-1]
    method_name = overview['method_name'][-1]
    if isinstance(changed_model, AbstractStateModel) and method_name in ['name'
        , 'script_text']:
        self.update_tab_label(changed_model)