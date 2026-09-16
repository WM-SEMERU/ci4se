def cookiecutter(template, checkout=None, no_input=False, extra_context=
    None, replay=False, overwrite_if_exists=False, output_dir='.',
    config_file=None, default_config=False, password=None):
    if replay and (no_input is not False or extra_context is not None):
        err_msg = (
            'You can not use both replay and no_input or extra_context at the same time.'
            )
        raise InvalidModeException(err_msg)
    config_dict = get_user_config(config_file=config_file, default_config=
        default_config)
    repo_dir, cleanup = determine_repo_dir(template=template, abbreviations
        =config_dict['abbreviations'], clone_to_dir=config_dict[
        'cookiecutters_dir'], checkout=checkout, no_input=no_input,
        password=password)
    template_name = os.path.basename(os.path.abspath(repo_dir))
    if replay:
        context = load(config_dict['replay_dir'], template_name)
    else:
        context_file = os.path.join(repo_dir, 'cookiecutter.json')
        logger.debug('context_file is {}'.format(context_file))
        context = generate_context(context_file=context_file,
            default_context=config_dict['default_context'], extra_context=
            extra_context)
        context['cookiecutter'] = prompt_for_config(context, no_input)
        context['cookiecutter']['_template'] = template
        dump(config_dict['replay_dir'], template_name, context)
    result = generate_files(repo_dir=repo_dir, context=context,
        overwrite_if_exists=overwrite_if_exists, output_dir=output_dir)
    if cleanup:
        rmtree(repo_dir)
    return result