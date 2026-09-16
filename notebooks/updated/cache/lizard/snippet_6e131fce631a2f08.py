def _parse_kexgss_complete(self, m):
    if self.transport.host_key is None:
        self.transport.host_key = NullHostKey()
    self.f = m.get_mpint()
    if self.f < 1 or self.f > self.P - 1:
        raise SSHException('Server kex "f" is out of range')
    mic_token = m.get_string()
    bool = m.get_boolean()
    srv_token = None
    if bool:
        srv_token = m.get_string()
    K = pow(self.f, self.x, self.P)
    hm = Message()
    hm.add(self.transport.local_version, self.transport.remote_version,
        self.transport.local_kex_init, self.transport.remote_kex_init)
    hm.add_string(self.transport.host_key.__str__())
    hm.add_mpint(self.e)
    hm.add_mpint(self.f)
    hm.add_mpint(K)
    H = sha1(str(hm)).digest()
    self.transport._set_K_H(K, H)
    if srv_token is not None:
        self.kexgss.ssh_init_sec_context(target=self.gss_host, recv_token=
            srv_token)
        self.kexgss.ssh_check_mic(mic_token, H)
    else:
        self.kexgss.ssh_check_mic(mic_token, H)
    self.transport.gss_kex_used = True
    self.transport._activate_outbound()