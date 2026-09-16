def _prepare_init_params_from_job_description(cls, job_details,
    model_channel_name=None):
    init_params = super(TensorFlow, cls
        )._prepare_init_params_from_job_description(job_details,
        model_channel_name)
    for argument in ('checkpoint_path', 'training_steps',
        'evaluation_steps', 'model_dir'):
        value = init_params['hyperparameters'].pop(argument, None)
        if value is not None:
            init_params[argument] = value
    image_name = init_params.pop('image')
    framework, py_version, tag, script_mode = fw.framework_name_from_image(
        image_name)
    if not framework:
        init_params['image_name'] = image_name
        return init_params
    if script_mode:
        init_params['script_mode'] = True
    init_params['py_version'] = py_version
    init_params['framework_version'
        ] = '1.4' if tag == '1.0' else fw.framework_version_from_tag(tag)
    training_job_name = init_params['base_job_name']
    if framework != cls.__framework_name__:
        raise ValueError(
            "Training job: {} didn't use image for requested framework".
            format(training_job_name))
    return init_params