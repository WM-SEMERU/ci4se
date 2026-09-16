def from_dict(cls, tx):
    inputs = [Input.from_dict(input_) for input_ in tx['inputs']]
    outputs = [Output.from_dict(output) for output in tx['outputs']]
    return cls(tx['operation'], tx['asset'], inputs, outputs, tx['metadata'
        ], tx['version'], hash_id=tx['id'])