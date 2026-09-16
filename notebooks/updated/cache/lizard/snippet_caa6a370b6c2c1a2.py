def validate(self, api_key=None):
    local_data = self.json_body
    if 'id' not in local_data or 'livemode' not in local_data:
        return False
    if self.is_test_event:
        logger.info('Test webhook received: {}'.format(local_data))
        return False
    if djstripe_settings.WEBHOOK_VALIDATION is None:
        return True
    elif djstripe_settings.WEBHOOK_VALIDATION == 'verify_signature' and djstripe_settings.WEBHOOK_SECRET:
        try:
            stripe.WebhookSignature.verify_header(self.body, self.headers.
                get('stripe-signature'), djstripe_settings.WEBHOOK_SECRET,
                djstripe_settings.WEBHOOK_TOLERANCE)
        except stripe.error.SignatureVerificationError:
            return False
        else:
            return True
    livemode = local_data['livemode']
    api_key = api_key or djstripe_settings.get_default_api_key(livemode)
    with stripe_temporary_api_version(local_data['api_version'], validate=False
        ):
        remote_data = Event.stripe_class.retrieve(id=local_data['id'],
            api_key=api_key)
    return local_data['data'] == remote_data['data']