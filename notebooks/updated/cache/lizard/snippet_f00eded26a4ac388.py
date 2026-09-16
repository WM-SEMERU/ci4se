def nbcompile(workdir, fileroot, html=True, basenb='', agdir=''):
    from shutil import copy
    from rtpipe import get_notebook
    from subprocess import call
    os.environ['fileroot'] = fileroot
    if agdir:
        os.environ['agdir'] = agdir
    if not basenb:
        basenb = get_notebook('baseinteract.ipynb')
    logger.info('Moving to {0} and building notebook for {1}'.format(
        workdir, fileroot))
    os.chdir(workdir)
    copy(basenb, '{0}/{1}.ipynb'.format(workdir, fileroot))
    cmd = (
        'jupyter nbconvert {0}.ipynb --inplace --execute --to notebook --allow-errors --ExecutePreprocessor.timeout=3600'
        .format(fileroot).split(' '))
    status = call(cmd)
    cmd = 'jupyter trust {0}.ipynb'.format(fileroot).split(' ')
    status = call(cmd)
    if html:
        cmd = 'jupyter nbconvert {0}.ipynb --to html --output {0}.html'.format(
            fileroot).split(' ')
        status = call(cmd)