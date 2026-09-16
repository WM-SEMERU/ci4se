def fetch_pdb(pdbid):
    pdbid = pdbid.lower()
    write_message('\nChecking status of PDB ID %s ... ' % pdbid)
    state, current_entry = check_pdb_status(pdbid)
    if state == 'OBSOLETE':
        write_message('entry is obsolete, getting %s instead.\n' %
            current_entry)
    elif state == 'CURRENT':
        write_message('entry is up to date.\n')
    elif state == 'UNKNOWN':
        sysexit(3, 'Invalid PDB ID (Entry does not exist on PDB server)\n')
    write_message('Downloading file from PDB ... ')
    pdburl = 'http://www.rcsb.org/pdb/files/%s.pdb' % current_entry
    try:
        pdbfile = urlopen(pdburl).read().decode()
        if 'sorry' in pdbfile:
            sysexit(5,
                'No file in PDB format available from wwPDB for the given PDB ID.\n'
                )
    except HTTPError:
        sysexit(5,
            'No file in PDB format available from wwPDB for the given PDB ID.\n'
            )
    return [pdbfile, current_entry]