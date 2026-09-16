def expire_record(record):
    load_message.cache_clear()
    orm.delete(pa for pa in model.PathAlias if pa.entry == record)
    record.delete()
    orm.commit()