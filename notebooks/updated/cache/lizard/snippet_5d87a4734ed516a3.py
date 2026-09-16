def GetClientOs(client_id, token=None):
    if data_store.RelationalDBEnabled():
        kb = data_store.REL_DB.ReadClientSnapshot(client_id).knowledge_base
    else:
        with aff4.FACTORY.Open(client_id, token=token) as client:
            kb = client.Get(client.Schema.KNOWLEDGE_BASE)
    return kb.os