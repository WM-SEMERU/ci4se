def get_queue_url(queue_name):
    client = boto3.client('sqs', CURRENT_REGION)
    queue = client.get_queue_url(QueueName=queue_name)
    return queue['QueueUrl']