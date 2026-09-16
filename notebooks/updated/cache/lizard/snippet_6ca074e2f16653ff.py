def publish(self, load):
    payload = {'enc': 'aes'}
    crypticle = salt.crypt.Crypticle(self.opts, salt.master.SMaster.secrets
        ['aes']['secret'].value)
    payload['load'] = crypticle.dumps(load)
    if self.opts['sign_pub_messages']:
        master_pem_path = os.path.join(self.opts['pki_dir'], 'master.pem')
        log.debug('Signing data packet')
        payload['sig'] = salt.crypt.sign_message(master_pem_path, payload[
            'load'])
    int_payload = {'payload': self.serial.dumps(payload)}
    if load['tgt_type'] == 'list':
        int_payload['topic_lst'] = load['tgt']
    match_targets = ['pcre', 'glob', 'list']
    if self.opts['zmq_filtering'] and load['tgt_type'] in match_targets:
        _res = self.ckminions.check_minions(load['tgt'], tgt_type=load[
            'tgt_type'])
        match_ids = _res['minions']
        log.debug('Publish Side Match: %s', match_ids)
        int_payload['topic_lst'] = match_ids
    payload = self.serial.dumps(int_payload)
    log.debug('Sending payload to publish daemon. jid=%s size=%d', load.get
        ('jid', None), len(payload))
    if not self.pub_sock:
        self.pub_connect()
    self.pub_sock.send(payload)
    log.debug('Sent payload to publish daemon.')