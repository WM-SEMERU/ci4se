def model(model_names):
    for model_name in model_names:
        context = {'name': model_name}
        render_template(template='common', context=context)
        render_template(template='model', context=context)