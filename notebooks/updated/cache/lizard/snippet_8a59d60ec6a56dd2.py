def run_message(message):
    if message.get('capture_response', False):
        DYNAMODB_CLIENT.put_item(TableName=ASYNC_RESPONSE_TABLE, Item={'id':
            {'S': str(message['response_id'])}, 'ttl': {'N': str(int(time.
            time() + 600))}, 'async_status': {'S': 'in progress'},
            'async_response': {'S': str(json.dumps('N/A'))}})
    func = import_and_get_task(message['task_path'])
    if hasattr(func, 'sync'):
        response = func.sync(*message['args'], **message['kwargs'])
    else:
        response = func(*message['args'], **message['kwargs'])
    if message.get('capture_response', False):
        DYNAMODB_CLIENT.update_item(TableName=ASYNC_RESPONSE_TABLE, Key={
            'id': {'S': str(message['response_id'])}}, UpdateExpression=
            'SET async_response = :r, async_status = :s',
            ExpressionAttributeValues={':r': {'S': str(json.dumps(response)
            )}, ':s': {'S': 'complete'}})
    return response