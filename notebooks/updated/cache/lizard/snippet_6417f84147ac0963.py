def finish_rel_branch(relver):
    print('finish release branch', relver)
    run('git flow release finish --keepremote -F -p -m "version {ver}" {ver}'
        .format(ver=relver), hide=True)