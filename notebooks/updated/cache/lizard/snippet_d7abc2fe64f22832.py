def cut(self, selection, smart_selection_adaption=False):
    assert isinstance(selection, Selection)
    import rafcon.gui.helpers.state_machine as gui_helper_state_machine
    if gui_helper_state_machine.is_selection_inside_of_library_state(
        selected_elements=selection.get_all()):
        logger.warning(
            'Cut is not performed because elements inside of a library state are selected.'
            )
        return
    selection_dict_of_copied_models, parent_m = (self.
        __create_core_and_model_object_copies(selection,
        smart_selection_adaption))
    non_empty_lists_dict, action_parent_m = self.get_action_arguments(
        parent_m if parent_m else None)
    action_parent_m.action_signal.emit(ActionSignalMsg(action='cut', origin
        ='clipboard', action_parent_m=action_parent_m, affected_models=[],
        after=False, kwargs={'remove': non_empty_lists_dict}))
    for models in selection_dict_of_copied_models.values():
        gui_helper_state_machine.delete_core_elements_of_models(models,
            destroy=True, recursive=True, force=False)
    affected_models = [model for models in non_empty_lists_dict.values() for
        model in models]
    action_parent_m.action_signal.emit(ActionSignalMsg(action='cut', origin
        ='clipboard', action_parent_m=action_parent_m, affected_models=
        affected_models, after=True))