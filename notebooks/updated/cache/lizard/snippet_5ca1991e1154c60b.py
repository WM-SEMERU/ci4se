def release(version):
    if version == '.':
        version = os.path.basename(root)
    existing_filenames = glob_blurbs(version)
    if existing_filenames:
        error(
            "Sorry, can't handle appending 'next' files to an existing version (yet)."
            )
    output = f('Misc/NEWS.d/{version}.rst')
    filenames = glob_blurbs('next')
    blurbs = Blurbs()
    date = current_date()
    if not filenames:
        print(f('No blurbs found.  Setting {version} as having no changes.'))
        body = f('There were no new changes in version {version}.\n')
        metadata = {'no changes': 'True', 'bpo': '0', 'section': 'Library',
            'date': date, 'nonce': nonceify(body)}
        blurbs.append((metadata, body))
    else:
        no_changes = None
        count = len(filenames)
        print(f('Merging {count} blurbs to "{output}".'))
        for filename in filenames:
            if not filename.endswith('.rst'):
                continue
            blurbs.load_next(filename)
        metadata = blurbs[0][0]
    metadata['release date'] = date
    print('Saving.')
    blurbs.save(output)
    git_add_files.append(output)
    flush_git_add_files()
    how_many = len(filenames)
    print(f("Removing {how_many} 'next' files from git."))
    git_rm_files.extend(filenames)
    flush_git_rm_files()
    blurbs2 = Blurbs()
    blurbs2.load(output)
    assert blurbs2 == blurbs, f("Reloading {output} isn't reproducible?!")
    print()
    print('Ready for commit.')