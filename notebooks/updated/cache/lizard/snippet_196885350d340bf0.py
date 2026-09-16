def submit_sms_conversion(self, message_id, delivered=True, timestamp=None):
    params = {'message-id': message_id, 'delivered': delivered, 'timestamp':
        timestamp or datetime.now(pytz.utc)}
    _format_date_param(params, 'timestamp')
    return self.post(self.api_host, '/conversions/sms', params)