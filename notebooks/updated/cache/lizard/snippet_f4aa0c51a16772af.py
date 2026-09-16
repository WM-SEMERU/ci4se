def concat(*args):
    if len(args) <= 0:
        raise PyrtlError('error, concat requires at least 1 argument')
    if len(args) == 1:
        return as_wires(args[0])
    arg_wirevectors = tuple(as_wires(arg) for arg in args)
    final_width = sum(len(arg) for arg in arg_wirevectors)
    outwire = WireVector(bitwidth=final_width)
    net = LogicNet(op='c', op_param=None, args=arg_wirevectors, dests=(
        outwire,))
    working_block().add_net(net)
    return outwire