def delete_stack(name=None, poll=0, timeout=60, profile=None):
    h_client = _auth(profile)
    ret = {'result': True, 'comment': ''}
    if not name:
        ret['result'] = False
        ret['comment'] = 'Parameter name missing or None'
        return ret
    try:
        h_client.stacks.delete(name)
    except heatclient.exc.HTTPNotFound:
        ret['result'] = False
        ret['comment'] = 'No stack {0}'.format(name)
    except heatclient.exc.HTTPForbidden as forbidden:
        log.exception(forbidden)
        ret['result'] = False
        ret['comment'] = six.text_type(forbidden)
    if ret['result'] is False:
        return ret
    if poll > 0:
        try:
            stack_status, msg = _poll_for_events(h_client, name, action=
                'DELETE', poll_period=poll, timeout=timeout)
        except heatclient.exc.CommandError:
            ret['comment'] = 'Deleted stack {0}.'.format(name)
            return ret
        except Exception as ex:
            log.exception('Delete failed %s', ex)
            ret['result'] = False
            ret['comment'] = '{0}'.format(ex)
            return ret
        if stack_status == 'DELETE_FAILED':
            ret['result'] = False
            ret['comment'] = "Deleted stack FAILED'{0}'{1}.".format(name, msg)
        else:
            ret['comment'] = 'Deleted stack {0}.'.format(name)
    return ret