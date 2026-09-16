def load(cls, keys):
    conversations = []
    for key in keys:
        conversation = unitdata.kv().get(key)
        if conversation:
            conversations.append(cls.deserialize(conversation))
    return conversations