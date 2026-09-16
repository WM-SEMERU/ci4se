def send(self, to, message):
    super(ProtobufProcess, self).send(to, message.DESCRIPTOR.full_name,
        message.SerializeToString())