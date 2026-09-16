def forward_message(self, peer: Peer, message: Message, on_success:
    callable=None):
    botapi.forward_message(peer.id, message.sender.id, message.id, **self.
        request_args).run()