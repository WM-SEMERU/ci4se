def _send(self, message):
    message['command'] = 'zappa.asynchronous.route_sns_task'
    payload = json.dumps(message).encode('utf-8')
    if len(payload) > LAMBDA_ASYNC_PAYLOAD_LIMIT:
        raise AsyncException('Payload too large for SNS')
    self.response = self.client.publish(TargetArn=self.arn, Message=payload)
    self.sent = self.response.get('MessageId')