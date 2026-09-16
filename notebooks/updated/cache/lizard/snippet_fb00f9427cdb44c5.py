def handler(event, context):
    records = deserialize_records(event['Records'])
    for record in records:
        process_dynamodb_differ_record(record, CurrentVPCModel, DurableVPCModel
            )