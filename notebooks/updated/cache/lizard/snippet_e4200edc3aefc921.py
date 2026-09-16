def prepare_state_m_for_insert_as(state_m_to_insert, previous_state_size):
    if isinstance(state_m_to_insert, AbstractStateModel
        ) and not gui_helper_meta_data.model_has_empty_meta(state_m_to_insert):
        if isinstance(state_m_to_insert, ContainerStateModel):
            models_dict = {'state': state_m_to_insert}
            for state_element_key in state_m_to_insert.state.state_element_attrs:
                state_element_list = getattr(state_m_to_insert,
                    state_element_key)
                if hasattr(state_element_list, 'keys'):
                    state_element_list = state_element_list.values()
                models_dict[state_element_key] = {elem.core_element.
                    core_element_id: elem for elem in state_element_list}
            resize_factor = (gui_helper_meta_data.
                scale_meta_data_according_state(models_dict, as_template=True))
            gui_helper_meta_data.resize_income_of_state_m(state_m_to_insert,
                resize_factor)
        elif isinstance(state_m_to_insert, StateModel):
            if previous_state_size:
                current_size = state_m_to_insert.get_meta_data_editor()['size']
                factor = gui_helper_meta_data.divide_two_vectors(current_size,
                    previous_state_size)
                state_m_to_insert.set_meta_data_editor('size',
                    previous_state_size)
                factor = min(*factor), min(*factor)
                gui_helper_meta_data.resize_state_meta(state_m_to_insert,
                    factor)
            else:
                logger.debug(
                    'For insert as template of {0} no resize of state meta data is performed because the meta data has empty fields.'
                    .format(state_m_to_insert))
        elif not isinstance(state_m_to_insert, LibraryStateModel):
            raise TypeError(
                'For insert as template of {0} no resize of state meta data is performed because state model type is not ContainerStateModel or StateModel'
                .format(state_m_to_insert))
    else:
        logger.info(
            'For insert as template of {0} no resize of state meta data is performed because the meta data has empty fields.'
            .format(state_m_to_insert))