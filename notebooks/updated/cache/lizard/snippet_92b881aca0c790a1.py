def format_log(ret):
    msg = ''
    if isinstance(ret, dict):
        if 'changes' in ret:
            chg = ret['changes']
            if not chg:
                if ret['comment']:
                    msg = ret['comment']
                else:
                    msg = 'No changes made for {0[name]}'.format(ret)
            elif isinstance(chg, dict):
                if 'diff' in chg:
                    if isinstance(chg['diff'], six.string_types):
                        msg = 'File changed:\n{0}'.format(chg['diff'])
                if all([isinstance(x, dict) for x in six.itervalues(chg)]):
                    if all([('old' in x and 'new' in x) for x in six.
                        itervalues(chg)]):
                        msg = 'Made the following changes:\n'
                        for pkg in chg:
                            old = chg[pkg]['old']
                            if not old and old not in (False, None):
                                old = 'absent'
                            new = chg[pkg]['new']
                            if not new and new not in (False, None):
                                new = 'absent'
                            msg += ("'{0}' changed from '{1}' to '{2}'\n".
                                format(pkg, old, new))
            if not msg:
                msg = six.text_type(ret['changes'])
            if ret['result'] is True or ret['result'] is None:
                log.info(msg)
            else:
                log.error(msg)
    else:
        log.info(six.text_type(ret))