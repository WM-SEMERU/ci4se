def change_message_visibility(self, queue, receipt_handle,
    visibility_timeout, callback=None):
    params = {'ReceiptHandle': receipt_handle, 'VisibilityTimeout':
        visibility_timeout}
    return self.get_status('ChangeMessageVisibility', params, queue.id,
        callback=callback)