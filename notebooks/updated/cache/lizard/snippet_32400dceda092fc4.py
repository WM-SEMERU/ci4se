def standalone_from_launchable(cls, launch):
    attrs = copy.copy(launch.el_attrs)
    del attrs['Type']
    if attrs.has_key('DependsOn'):
        del attrs['DependsOn']
    if attrs['Properties'].has_key('SpotPrice'):
        del attrs['Properties']['SpotPrice']
    if attrs['Properties'].has_key('InstanceMonitoring'):
        del attrs['Properties']['InstanceMonitoring']
    if attrs['Properties'].has_key('SecurityGroups'):
        del attrs['Properties']['SecurityGroups']
    if attrs['Properties'].has_key('InstanceId'):
        raise RuntimeError(
            "Can't make instance from launchable containing InstanceId property"
            )
    inst = EC2Instance(**attrs)
    inst.iscm = launch.iscm
    return inst