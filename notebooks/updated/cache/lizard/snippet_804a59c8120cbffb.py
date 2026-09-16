def sync_entities(*model_objs):
    if sync_entities.defer:
        if not model_objs:
            sync_entities.buffer[None] = None
        else:
            for model_obj in model_objs:
                sync_entities.buffer[model_obj.__class__, model_obj.pk
                    ] = model_obj
        return False
    EntitySyncer(*model_objs).sync()