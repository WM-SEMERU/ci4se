def on_response(self, ch, method_frame, props, body):
    LOGGER.debug('rabbitmq.Requester.on_response')
    if self.corr_id == props.correlation_id:
        self.response = {'props': props, 'body': body}
    else:
        LOGGER.warn(
            'rabbitmq.Requester.on_response - discarded response : ' + str(
            props.correlation_id))
        LOGGER.debug('natsd.Requester.on_response - discarded response : ' +
            str({'properties': props, 'body': body}))