def get_instance(cls, dependencies=None):
    assert cls is not ContractBase, 'ContractBase is not meant to be used directly.'
    assert cls.CONTRACT_NAME, 'CONTRACT_NAME must be set to a valid keeper contract name.'
    return cls(cls.CONTRACT_NAME, dependencies)