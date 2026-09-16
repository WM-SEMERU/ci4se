def AddContract(self, contract):
    super(UserWallet, self).AddContract(contract)
    try:
        db_contract = Contract.get(ScriptHash=contract.ScriptHash.ToBytes())
        db_contract.delete_instance()
    except Exception as e:
        logger.debug('contract does not exist yet')
    sh = bytes(contract.ScriptHash.ToArray())
    address, created = Address.get_or_create(ScriptHash=sh)
    address.IsWatchOnly = False
    address.save()
    db_contract = Contract.create(RawData=contract.ToArray(), ScriptHash=
        contract.ScriptHash.ToBytes(), PublicKeyHash=contract.PublicKeyHash
        .ToBytes(), Address=address, Account=self.__dbaccount)
    logger.debug('Creating db contract %s ' % db_contract)
    db_contract.save()