def get_service(service, model_form='models', form_name=''):
    service_name = str(service).split('Service')[1]
    class_name = 'th_' + service_name.lower() + '.' + model_form
    if model_form == 'forms':
        return class_for_name(class_name, service_name + form_name)
    else:
        return class_for_name(class_name, service_name)