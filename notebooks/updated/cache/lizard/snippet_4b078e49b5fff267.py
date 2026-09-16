def reprovision(vm, image, key='uuid'):
    ret = {}
    if key not in ['uuid', 'alias', 'hostname']:
        ret['Error'] = 'Key must be either uuid, alias or hostname'
        return ret
    vm = lookup('{0}={1}'.format(key, vm), one=True)
    if 'Error' in vm:
        return vm
    if image not in __salt__['imgadm.list']():
        ret['Error'] = 'Image ({0}) is not present on this host'.format(image)
        return ret
    cmd = six.text_type('echo {image} | vmadm reprovision {uuid}').format(uuid
        =salt.utils.stringutils.to_unicode(vm), image=_quote_args(salt.
        utils.json.dumps({'image_uuid': image})))
    res = __salt__['cmd.run_all'](cmd, python_shell=True)
    retcode = res['retcode']
    if retcode != 0:
        ret['Error'] = res['stderr'] if 'stderr' in res else _exit_status(
            retcode)
        return ret
    return True