def is_deterministic(self):
    patterns = [t.lhs for t in self.transitions] + list(self.accept_configs)
    for i, t1 in enumerate(patterns):
        for t2 in patterns[:i]:
            match = True
            for in1, in2 in zip(t1, t2):
                i = max(-in1.position, -in2.position)
                while i + in1.position < len(in1) and i + in2.position < len(
                    in2):
                    x1 = in1.values[i + in1.position]
                    x2 = in2.values[i + in2.position]
                    if x1 != x2:
                        match = False
                    i += 1
            if match:
                return False
    return True