def accepts(self, tp, converter):
    tp = ParameterizedProperty._validate_type_param(tp)
    self.alternatives.append((tp, converter))
    return self