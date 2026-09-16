def param_labels(self):
    paramnames_labels = []
    prior_class_dict = self.variable.prior_class_dict
    prior_prior_model_dict = self.variable.prior_prior_model_dict
    for prior_name, prior in self.variable.prior_tuples_ordered_by_id:
        param_string = self.label_config.label(prior_name)
        prior_model = prior_prior_model_dict[prior]
        cls = prior_class_dict[prior]
        cls_string = '{}{}'.format(self.label_config.subscript(cls), 
            prior_model.component_number + 1)
        param_label = '{}_{{\\mathrm{{{}}}}}'.format(param_string, cls_string)
        paramnames_labels.append(param_label)
    return paramnames_labels