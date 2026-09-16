def UpdateHunt(hunt_id, client_limit=None, client_rate=None, duration=None):
    hunt_obj = data_store.REL_DB.ReadHuntObject(hunt_id)
    if hunt_obj.hunt_state != hunt_obj.HuntState.PAUSED:
        raise OnlyPausedHuntCanBeModifiedError(hunt_obj)
    data_store.REL_DB.UpdateHuntObject(hunt_id, client_limit=client_limit,
        client_rate=client_rate, duration=duration)
    return data_store.REL_DB.ReadHuntObject(hunt_id)