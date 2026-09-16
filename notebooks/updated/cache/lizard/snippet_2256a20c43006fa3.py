def run(args):
    kwargs = vars(args)
    if 'func' in kwargs:
        del kwargs['func']
    project_path = kwargs.pop('project_path')
    config = configure(project_path, kwargs.get('config_file'))
    output_dir = kwargs.pop('output_dir', None) or generate_output_path(args,
        project_path)
    stats_handler.init_stats(output_dir, config)
    topic = args.publisher_channel or uuid.uuid4().hex
    print('External publishing topic is %s' % topic)
    start_hq(output_dir, config, topic, **kwargs)
    if not args.no_results:
        process_results(output_dir, config)
    copy_config(project_path, output_dir)
    print('done.\n')