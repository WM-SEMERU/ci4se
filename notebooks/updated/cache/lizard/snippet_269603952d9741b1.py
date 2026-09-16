def _get_validated_json(json_spec, args):
    if not json_spec:
        return
    if not args:
        return
    validated_spec = copy.deepcopy(json_spec)
    unsupported_keys = _get_unsupported_keys(validated_spec.keys(),
        SUPPORTED_KEYS)
    if len(unsupported_keys) > 0:
        logger.warn(
            'Warning: the following root level fields are not supported and will be ignored: {}'
            .format(', '.join(unsupported_keys)))
    if 'stages' in validated_spec:
        validated_spec['stages'] = _get_validated_stages(validated_spec[
            'stages'])
    if 'name' in validated_spec:
        if args.src_dir != validated_spec['name']:
            logger.warn(
                'workflow name "%s" does not match containing directory "%s"' %
                (validated_spec['name'], args.src_dir))
    if 'ignoreReuse' in validated_spec:
        validate_ignore_reuse(validated_spec['stages'], validated_spec[
            'ignoreReuse'])
    validated_documentation_fields = _get_validated_json_for_build_or_update(
        validated_spec, args)
    validated_spec.update(validated_documentation_fields)
    if args.mode == 'workflow':
        validated = _validate_json_for_regular_workflow(json_spec, args)
        validated_spec.update(validated)
    if args.mode == 'globalworkflow':
        _validate_json_for_global_workflow(validated_spec, args)
    return validated_spec