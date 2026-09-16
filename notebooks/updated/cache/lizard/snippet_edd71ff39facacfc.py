def where_entry_deleted(query):
    return orm.select(e for e in query if e.status == model.PublishStatus.
        GONE.value)