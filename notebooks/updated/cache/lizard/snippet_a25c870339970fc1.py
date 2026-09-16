def FB(circuit, *, out_port=None, in_port=None):
    if out_port is None:
        out_port = circuit.cdim - 1
    if in_port is None:
        in_port = circuit.cdim - 1
    return Feedback.create(circuit, out_port=out_port, in_port=in_port)