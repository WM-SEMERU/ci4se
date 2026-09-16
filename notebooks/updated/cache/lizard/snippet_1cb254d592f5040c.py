def _activate(self, token):
    info = token.to_info()
    activation = Activation(self.rule, frozenset(info.data), {k: v for k, v in
        info.context if isinstance(k, str)})
    if token.is_valid():
        if info not in self.memory:
            self.memory.add(info)
            if activation in self.removed:
                self.removed.remove(activation)
            else:
                self.added.add(activation)
    else:
        try:
            self.memory.remove(info)
        except ValueError:
            pass
        else:
            if activation in self.added:
                self.added.remove(activation)
            else:
                self.removed.add(activation)