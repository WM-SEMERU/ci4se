def write_example_yaml(cls, dest, skip=()):
    inst = cls.example_instance(skip=skip)
    with open(dest, 'w') as f:
        inst.to_yaml(stream=f, skip=skip)