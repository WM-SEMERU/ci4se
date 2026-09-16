def upgradeCatalog1to2(oldCatalog):
    newCatalog = oldCatalog.upgradeVersion('tag_catalog', 1, 2, tagCount=
        oldCatalog.tagCount)
    tags = newCatalog.store.query(Tag, Tag.catalog == newCatalog)
    tagNames = tags.getColumn('name').distinct()
    for t in tagNames:
        _TagName(store=newCatalog.store, catalog=newCatalog, name=t)
    return newCatalog