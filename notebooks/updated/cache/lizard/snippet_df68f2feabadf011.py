def insertUserStore(siteStore, userStorePath):
    ls = siteStore.findUnique(LoginSystem)
    unattachedSubStore = Store(userStorePath)
    for lm in unattachedSubStore.query(LoginMethod, LoginMethod.account ==
        unattachedSubStore.findUnique(LoginAccount), sort=LoginMethod.
        internal.descending):
        if ls.accountByAddress(lm.localpart, lm.domain) is None:
            localpart, domain = lm.localpart, lm.domain
            break
    else:
        raise AllNamesConflict()
    unattachedSubStore.close()
    insertLocation = siteStore.newFilePath('account', domain, localpart +
        '.axiom')
    insertParentLoc = insertLocation.parent()
    if not insertParentLoc.exists():
        insertParentLoc.makedirs()
    if insertLocation.exists():
        raise DatabaseDirectoryConflict()
    userStorePath.moveTo(insertLocation)
    ss = SubStore(store=siteStore, storepath=insertLocation)
    attachedStore = ss.open()
    attachedStore.findUnique(LoginAccount).migrateUp()