def try_one_generator_really(project, name, generator, target_type,
    properties, sources):
    if __debug__:
        from .targets import ProjectTarget
        assert isinstance(project, ProjectTarget)
        assert isinstance(name, basestring) or name is None
        assert isinstance(generator, Generator)
        assert isinstance(target_type, basestring)
        assert isinstance(properties, property_set.PropertySet)
        assert is_iterable_typed(sources, virtual_target.VirtualTarget)
    targets = generator.run(project, name, properties, sources)
    usage_requirements = []
    success = False
    dout('returned ' + str(targets))
    if targets:
        success = True
        if isinstance(targets[0], property_set.PropertySet):
            usage_requirements = targets[0]
            targets = targets[1]
        else:
            usage_requirements = property_set.empty()
    dout('  generator' + generator.id() + ' spawned ')
    if success:
        return usage_requirements, targets
    else:
        return None