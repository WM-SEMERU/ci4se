def absent(name, force=False, region=None, key=None, keyid=None, profile=
    None, remove_lc=False):
    ret = {'name': name, 'result': True, 'comment': '', 'changes': {}}
    asg = __salt__['boto_asg.get_config'](name, region, key, keyid, profile)
    if asg is None:
        ret['result'] = False
        ret['comment'] = 'Failed to check autoscale group existence.'
    elif asg:
        if __opts__['test']:
            ret['comment'] = 'Autoscale group set to be deleted.'
            ret['result'] = None
            if remove_lc:
                msg = 'Launch configuration {0} is set to be deleted.'.format(
                    asg['launch_config_name'])
                ret['comment'] = ' '.join([ret['comment'], msg])
            return ret
        deleted = __salt__['boto_asg.delete'](name, force, region, key,
            keyid, profile)
        if deleted:
            if remove_lc:
                lc_deleted = __salt__['boto_asg.delete_launch_configuration'](
                    asg['launch_config_name'], region, key, keyid, profile)
                if lc_deleted:
                    if 'launch_config' not in ret['changes']:
                        ret['changes']['launch_config'] = {}
                    ret['changes']['launch_config']['deleted'] = asg[
                        'launch_config_name']
                else:
                    ret['result'] = False
                    ret['comment'] = ' '.join([ret['comment'],
                        'Failed to delete launch configuration.'])
            ret['changes']['old'] = asg
            ret['changes']['new'] = None
            ret['comment'] = 'Deleted autoscale group.'
        else:
            ret['result'] = False
            ret['comment'] = 'Failed to delete autoscale group.'
    else:
        ret['comment'] = 'Autoscale group does not exist.'
    return ret