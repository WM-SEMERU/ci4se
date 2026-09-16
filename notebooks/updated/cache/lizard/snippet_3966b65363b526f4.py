def get_version(self):
    data = self.message(MessageType.GET_VERSION, '')
    return json.loads(data, object_hook=VersionReply)