def update_models(self, model, name, info):
    if info.method_name in ['add_input_data_port', 'remove_input_data_port',
        'input_data_ports']:
        model_list, data_list, model_name, model_class, model_key = (self.
            get_model_info('input_data_port'))
    elif info.method_name in ['add_output_data_port',
        'remove_output_data_port', 'output_data_ports']:
        model_list, data_list, model_name, model_class, model_key = (self.
            get_model_info('output_data_port'))
    elif info.method_name in ['add_income', 'remove_income', 'income']:
        model_list, data_list, model_name, model_class, model_key = (self.
            get_model_info('income'))
    elif info.method_name in ['add_outcome', 'remove_outcome', 'outcomes']:
        model_list, data_list, model_name, model_class, model_key = (self.
            get_model_info('outcome'))
    else:
        return
    if 'add' in info.method_name:
        self.add_missing_model(model_list, data_list, model_name,
            model_class, model_key)
    elif 'remove' in info.method_name:
        destroy = info.kwargs.get('destroy', True)
        self.remove_specific_model(model_list, info.result, model_key, destroy)
    elif info.method_name in ['input_data_ports', 'output_data_ports',
        'income', 'outcomes']:
        self.re_initiate_model_list(model_list, data_list, model_name,
            model_class, model_key)