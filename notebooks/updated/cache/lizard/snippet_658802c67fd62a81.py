def checkValidNodeTypes(provisioner, nodeTypes):
    if not nodeTypes:
        return
    if not isinstance(nodeTypes, list):
        nodeTypes = [nodeTypes]
    if not isinstance(nodeTypes[0], string_types):
        return
    from toil.lib.generatedEC2Lists import E2Instances, regionDict
    if provisioner == 'aws':
        from toil.provisioners.aws import getCurrentAWSZone
        currentZone = getCurrentAWSZone()
        if not currentZone:
            currentZone = 'us-west-2'
        else:
            currentZone = currentZone[:-1]
        for nodeType in nodeTypes:
            if nodeType and ':' in nodeType:
                nodeType = nodeType.split(':')[0]
            if nodeType not in regionDict[currentZone]:
                close = get_close_matches(nodeType, regionDict[currentZone], 1)
                if len(close) > 0:
                    helpText = ' Did you mean ' + close[0] + '?'
                else:
                    helpText = ''
                raise RuntimeError(
                    'Invalid nodeType (%s) specified for AWS in region: %s.%s'
                     % (nodeType, currentZone, helpText))
    if provisioner == 'gce' or provisioner == 'azure':
        for nodeType in nodeTypes:
            if nodeType and ':' in nodeType:
                nodeType = nodeType.split(':')[0]
            try:
                E2Instances[nodeType]
                raise RuntimeError(
                    "It looks like you've specified an AWS nodeType with the {} provisioner.  Please specify an {} nodeType."
                    .format(provisioner, provisioner))
            except KeyError:
                pass