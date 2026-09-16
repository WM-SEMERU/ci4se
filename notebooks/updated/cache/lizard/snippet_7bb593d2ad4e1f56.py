def resize_state_port_meta(state_m, factor, gaphas_editor=True):
    if not gaphas_editor and isinstance(state_m, ContainerStateModel):
        port_models = state_m.input_data_ports[:] + state_m.output_data_ports[:
            ] + state_m.scoped_variables[:]
    else:
        port_models = state_m.input_data_ports[:] + state_m.output_data_ports[:
            ] + state_m.outcomes[:]
        port_models += state_m.scoped_variables[:] if isinstance(state_m,
            ContainerStateModel) else []
    _resize_port_models_list(port_models, 'rel_pos' if gaphas_editor else
        'inner_rel_pos', factor, gaphas_editor)
    resize_income_of_state_m(state_m, factor, gaphas_editor)