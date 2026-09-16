def ProcessResponse(self, state, response):
    emails_left = self.args.emails_limit - self.IncrementCounter()
    if emails_left < 0:
        return
    if data_store.RelationalDBEnabled():
        client_id = response.source.Basename()
        client = data_store.REL_DB.ReadClientSnapshot(client_id)
        hostname = client.knowledge_base.fqdn or 'unknown hostname'
        client_fragment_id = '/clients/%s' % client_id
    else:
        client_id = response.source
        client = aff4.FACTORY.Open(client_id, token=self.token)
        hostname = client.Get(client.Schema.HOSTNAME) or 'unknown hostname'
        client_fragment_id = '/clients/%s' % client_id.Basename()
    if emails_left == 0:
        additional_message = self.too_many_mails_msg % self.args.emails_limit
    else:
        additional_message = ''
    subject = self.__class__.subject_template.render(source_urn=utils.
        SmartUnicode(self.source_urn))
    body = self.__class__.template.render(client_id=client_id,
        client_fragment_id=client_fragment_id, admin_ui_url=config.CONFIG[
        'AdminUI.url'], source_urn=self.source_urn, additional_message=
        additional_message, signature=config.CONFIG['Email.signature'],
        hostname=utils.SmartUnicode(hostname), creator=utils.SmartUnicode(
        self.token.username))
    email_alerts.EMAIL_ALERTER.SendEmail(self.args.email_address,
        'grr-noreply', utils.SmartStr(subject), utils.SmartStr(body),
        is_html=True)