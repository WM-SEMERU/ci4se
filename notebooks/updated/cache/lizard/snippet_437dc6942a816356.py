def get_git_info():
    start_dir = abspath(curdir)
    try:
        chdir(dirname(abspath(__file__)))
        re_patt_str = (
            'commit\\s+(?P<commit_hash>\\w+).*?Author:\\s+(?P<author_name>.*?)\\s+<(?P<author_email>.*?)>\\s+Date:\\s+(?P<date>.*?)\\n\\s+(?P<commit_msg>.*?)(?:\\ndiff.*?)?$'
            )
        show_out = check_output(['git', 'show']).decode('ascii')
        revp_out = check_output(['git', 'rev-parse', '--abbrev-ref', 'HEAD'])
        revp_out = revp_out.decode('ascii').strip()
        m = re.search(re_patt_str, show_out, re.DOTALL)
        assert m is not None, 'Regex pattern:\n\n"%s"\n\n failed to match string:\n\n"%s"' % (
            re_patt_str, show_out)
        ret_dict = m.groupdict()
        ret_dict['branch_name'] = revp_out
    finally:
        chdir(start_dir)
    return ret_dict