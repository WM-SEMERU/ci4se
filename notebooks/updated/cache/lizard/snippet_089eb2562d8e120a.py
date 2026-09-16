def _updateConstructorAndMembers(self):
    syntheticMetaData = self._syntheticMetaData()
    constructor = self._constructorFactory.makeConstructor(syntheticMetaData
        .originalConstructor(), syntheticMetaData.syntheticMemberList(),
        syntheticMetaData.doesConsumeArguments())
    self._class.__init__ = constructor
    for syntheticMember in syntheticMetaData.syntheticMemberList():
        syntheticMember.apply(self._class, syntheticMetaData.
            originalMemberNameList(), syntheticMetaData.namingConvention())
    if syntheticMetaData.hasEqualityGeneration():
        eq = self._comparisonFactory.makeEqualFunction(syntheticMetaData.
            originalEqualFunction(), syntheticMetaData.syntheticMemberList())
        ne = self._comparisonFactory.makeNotEqualFunction(syntheticMetaData
            .originalNotEqualFunction(), syntheticMetaData.
            syntheticMemberList())
        hashFunc = self._comparisonFactory.makeHashFunction(syntheticMetaData
            .originalHashFunction(), syntheticMetaData.syntheticMemberList())
        self._class.__eq__ = eq
        self._class.__ne__ = ne
        self._class.__hash__ = hashFunc