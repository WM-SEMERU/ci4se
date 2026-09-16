def _validateIterCommonParams(MaxObjectCount, OperationTimeout):
    if MaxObjectCount is None or MaxObjectCount <= 0:
        raise ValueError(_format('MaxObjectCount must be > 0 but is {0}',
            MaxObjectCount))
    if OperationTimeout is not None and OperationTimeout < 0:
        raise ValueError(_format('OperationTimeout must be >= 0 but is {0}',
            OperationTimeout))