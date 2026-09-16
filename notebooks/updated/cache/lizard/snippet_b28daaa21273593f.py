def from_gapic(operation, operations_client, result_type, **kwargs):
    refresh = functools.partial(operations_client.get_operation, operation.name
        )
    cancel = functools.partial(operations_client.cancel_operation,
        operation.name)
    return Operation(operation, refresh, cancel, result_type, **kwargs)