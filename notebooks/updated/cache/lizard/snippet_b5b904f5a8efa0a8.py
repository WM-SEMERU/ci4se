def build_operation(operation, ns, rule, func):
    swagger_operation = swagger.Operation(operationId=operation_name(
        operation, ns), parameters=swagger.ParametersList([]), responses=
        swagger.Responses(), tags=[ns.subject_name])
    swagger_operation.parameters.append(header_param('X-Response-Skip-Null'))
    swagger_operation.parameters.extend([path_param(argument, ns) for
        argument in rule.arguments])
    qs_schema = get_qs_schema(func)
    if qs_schema:
        swagger_operation.parameters.extend([query_param(name, field) for 
            name, field in qs_schema.fields.items()])
    request_schema = get_request_schema(func)
    if request_schema:
        swagger_operation.parameters.append(body_param(request_schema))
    swagger_operation.parameters.sort(key=lambda parameter: parameter['name'])
    add_responses(swagger_operation, operation, ns, func)
    return swagger_operation