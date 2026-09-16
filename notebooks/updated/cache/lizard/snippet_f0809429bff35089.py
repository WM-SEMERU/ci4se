def list_packet_names(self):
    path = '/archive/{}/packet-names'.format(self._instance)
    response = self._client.get_proto(path=path)
    message = archive_pb2.GetPacketNamesResponse()
    message.ParseFromString(response.content)
    names = getattr(message, 'name')
    return iter(names)