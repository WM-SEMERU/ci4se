def validate_parsed_json(obj_json, options=None):
    validating_list = isinstance(obj_json, list)
    if not options:
        options = ValidationOptions()
    if not options.no_cache:
        init_requests_cache(options.refresh_cache)
    results = None
    if validating_list:
        results = []
        for obj in obj_json:
            try:
                results.append(validate_instance(obj, options))
            except SchemaInvalidError as ex:
                error_result = ObjectValidationResults(is_valid=False,
                    object_id=obj.get('id', ''), errors=[str(ex)])
                results.append(error_result)
    else:
        try:
            results = validate_instance(obj_json, options)
        except SchemaInvalidError as ex:
            error_result = ObjectValidationResults(is_valid=False,
                object_id=obj_json.get('id', ''), errors=[str(ex)])
            results = error_result
    if not options.no_cache and options.clear_cache:
        clear_requests_cache()
    return results