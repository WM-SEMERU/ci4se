def ToParameter(item: StackItem):
    if isinstance(item, Array) or isinstance(item, Struct):
        items = item.GetArray()
        output = [ContractParameter.ToParameter(subitem) for subitem in items]
        return ContractParameter(type=ContractParameterType.Array, value=output
            )
    elif isinstance(item, Boolean):
        return ContractParameter(type=ContractParameterType.Boolean, value=
            item.GetBoolean())
    elif isinstance(item, ByteArray):
        return ContractParameter(type=ContractParameterType.ByteArray,
            value=item.GetByteArray())
    elif isinstance(item, Integer):
        return ContractParameter(type=ContractParameterType.Integer, value=
            str(item.GetBigInteger()))
    elif isinstance(item, InteropInterface):
        return ContractParameter(type=ContractParameterType.
            InteropInterface, value=item.GetInterface())