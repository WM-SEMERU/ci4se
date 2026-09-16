def post(self, request):
    self.request = request
    self.target = request.GET.get('TARGET')
    self.root = etree.fromstring(request.body)
    try:
        self.ticket = self.process_ticket()
        expire_instant = (self.ticket.creation + timedelta(seconds=self.
            ticket.VALIDITY)).isoformat()
        params = {'IssueInstant': timezone.now().isoformat(),
            'expireInstant': expire_instant, 'Recipient': self.target,
            'ResponseID': utils.gen_saml_id(), 'username': self.ticket.
            username(), 'attributes': self.ticket.attributs_flat(),
            'auth_date': self.ticket.user.last_login.replace(microsecond=0)
            .isoformat(), 'is_new_login': 'true' if self.ticket.renew else
            'false'}
        logger.info(
            'SamlValidate: ticket %s validated for user %s on service %s.' %
            (self.ticket.value, self.ticket.user.username, self.ticket.service)
            )
        logger.debug('SamlValidate: User attributes are:\n%s' % pprint.
            pformat(self.ticket.attributs))
        return render(request, 'cas_server/samlValidate.xml', params,
            content_type='text/xml; charset=utf-8')
    except SamlValidateError as error:
        logger.warning('SamlValidate: validation error: %s %s' % (error.
            code, error.msg))
        return error.render(request)