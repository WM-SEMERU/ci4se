def auth_send(self):
    assert len(self.packets) == 2
    packet = Packet(exchange_type=const.ExchangeType.IKE_AUTH, iSPI=self.
        iSPI, rSPI=self.rSPI)
    id_payload = payloads.IDi()
    packet.add_payload(id_payload)
    signed_octets = bytes(self.packets[0]) + self.Nr + prf(self.SK_pi,
        id_payload._data)
    packet.add_payload(payloads.AUTH(signed_octets))
    self.esp_SPIout = int.from_bytes(os.urandom(4), 'big')
    packet.add_payload(payloads.SA(proposals=[proposal.Proposal(protocol=
        const.ProtocolID.ESP, spi=self.esp_SPIout, last=True, transforms=[(
        'ENCR_CAMELLIA_CBC', 256), ('ESN',), ('AUTH_HMAC_SHA2_256_128',)])]))
    packet.add_payload(payloads.TSi(addr=self.address))
    packet.add_payload(payloads.TSr(addr=self.peer))
    packet.add_payload(payloads.Notify(notify_type=const.MessageType.
        INITIAL_CONTACT))
    self.packets.append(packet)
    self.state = State.AUTH
    return self.encrypt_and_hmac(packet)