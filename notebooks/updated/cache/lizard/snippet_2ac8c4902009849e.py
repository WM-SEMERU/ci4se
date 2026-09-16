def dump_model_data(request, app_label, model_label):
    return dump_to_response(request, '%s.%s' % (app_label, model_label), [],
        '-'.join((app_label, model_label)))