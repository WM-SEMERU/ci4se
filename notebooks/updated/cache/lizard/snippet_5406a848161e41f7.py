def write_changelog(debug=False):
    changelog = _iter_log_oneline(debug)
    if changelog:
        changelog = _iter_changelog(changelog)
    if not changelog:
        return
    if debug:
        print('Writing ChangeLog')
    new_changelog = os.path.join(os.path.curdir, 'ChangeLog')
    if os.path.exists(new_changelog) and not os.access(new_changelog, os.W_OK):
        return
    with io.open(new_changelog, 'w', encoding='utf-8') as changelog_file:
        for release, content in changelog:
            changelog_file.write(content)