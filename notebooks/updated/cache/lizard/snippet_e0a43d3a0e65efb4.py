def subcomponents(self, subcomponents):
    for arg in self.args:
        if arg.__class__.__name__ == 'Function':
            subcomponents.append(arg.to_string())
            if arg.function_type == 'primary':
                arg.subcomponents(subcomponents)
        else:
            subcomponents.append(arg.to_string())
    return subcomponents