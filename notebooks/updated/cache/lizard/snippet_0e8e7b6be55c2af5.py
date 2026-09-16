def meta_changed_notify_after(self, state_machine_m, _, info):
    meta_signal_message = info['arg']
    if meta_signal_message.origin == 'graphical_editor_gaphas':
        return
    if meta_signal_message.origin == 'load_meta_data':
        return
    notification = meta_signal_message.notification
    if not notification:
        return
    if self.model.ongoing_complex_actions:
        return
    model = notification.model
    view = self.canvas.get_view_for_model(model)
    if meta_signal_message.change == 'show_content':
        library_state_m = model
        library_state_v = view
        if library_state_m.meta['gui']['show_content'
            ] is not library_state_m.show_content():
            logger.warning(
                "The content of the LibraryState won't be shown, because MAX_VISIBLE_LIBRARY_HIERARCHY is 1."
                )
        if library_state_m.show_content():
            if not library_state_m.state_copy_initialized:
                logger.warning(
                    'Show library content without initialized state copy does not work {0}'
                    .format(library_state_m))
            logger.debug('Show content of {}'.format(library_state_m.state))
            gui_helper_meta_data.scale_library_content(library_state_m)
            self.add_state_view_for_model(library_state_m.state_copy, view,
                hierarchy_level=library_state_v.hierarchy_level + 1)
        else:
            logger.debug('Hide content of {}'.format(library_state_m.state))
            state_copy_v = self.canvas.get_view_for_model(library_state_m.
                state_copy)
            if state_copy_v:
                state_copy_v.remove()
    elif isinstance(view, StateView):
        view.apply_meta_data(recursive=meta_signal_message.affects_children)
    else:
        view.apply_meta_data()
    self.canvas.request_update(view, matrix=True)
    self.canvas.wait_for_update()