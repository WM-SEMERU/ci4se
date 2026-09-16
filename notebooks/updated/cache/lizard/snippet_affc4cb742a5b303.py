def _tarjan(self, function, order, stack, data):
    try:
        func_data = data[function.id]
        return order
    except KeyError:
        func_data = self._TarjanData(order)
        data[function.id] = func_data
    order += 1
    pos = len(stack)
    stack.append(function)
    func_data.onstack = True
    for call in compat_itervalues(function.calls):
        try:
            callee_data = data[call.callee_id]
            if callee_data.onstack:
                func_data.lowlink = min(func_data.lowlink, callee_data.order)
        except KeyError:
            callee = self.functions[call.callee_id]
            order = self._tarjan(callee, order, stack, data)
            callee_data = data[call.callee_id]
            func_data.lowlink = min(func_data.lowlink, callee_data.lowlink)
    if func_data.lowlink == func_data.order:
        members = stack[pos:]
        del stack[pos:]
        if len(members) > 1:
            cycle = Cycle()
            for member in members:
                cycle.add_function(member)
                data[member.id].onstack = False
        else:
            for member in members:
                data[member.id].onstack = False
    return order