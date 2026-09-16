def evaluate(self, instance, step, extra):
    chain = step.chain[1:]
    if self.strict and not chain:
        raise TypeError(
            "A ContainerAttribute in 'strict' mode can only be used within a SubFactory."
            )
    return self.function(instance, chain)