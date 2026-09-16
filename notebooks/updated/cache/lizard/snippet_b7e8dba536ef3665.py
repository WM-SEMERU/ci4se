def no_retry_on_failure(handler):
    seen_request_ids = set()

    @wraps(handler)
    def wrapper(event, context):
        if context.aws_request_id in seen_request_ids:
            logger.critical('Retry attempt on request id %s detected.',
                context.aws_request_id)
            return {'statusCode': 200}
        seen_request_ids.add(context.aws_request_id)
        return handler(event, context)
    return wrapper