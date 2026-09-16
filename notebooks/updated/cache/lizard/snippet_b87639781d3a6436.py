def encode_hooklist(self, hooklist, msg):
    for hook in hooklist:
        pbhook = msg.add()
        self.encode_hook(hook, pbhook)