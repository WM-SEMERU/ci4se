def dumper(args, config, transform_func=None):
    args = process_args(args)
    submit_args = get_submit_args(args)
    submit_outcome = submit_if_ready(args, submit_args, config)
    if submit_outcome is not None:
        return submit_outcome
    import_time = datetime.datetime.utcnow()
    try:
        records = dump2polarion.import_results(args.input_file, older_than=
            import_time)
        testrun_id = get_testrun_id(args, config, records.testrun)
        exporter = dump2polarion.XunitExport(testrun_id, records, config,
            transform_func=transform_func)
        output = exporter.export()
    except NothingToDoException as info:
        logger.info(info)
        return 0
    except (EnvironmentError, Dump2PolarionException) as err:
        logger.fatal(err)
        return 1
    if args.output_file or args.no_submit:
        exporter.write_xml(output, args.output_file)
    if not args.no_submit:
        response = dump2polarion.submit_and_verify(output, config=config,
            **submit_args)
        __, ext = os.path.splitext(args.input_file)
        if ext.lower() in dbtools.SQLITE_EXT and response:
            dbtools.mark_exported_sqlite(args.input_file, import_time)
        return 0 if response else 2
    return 0