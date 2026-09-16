def action_bootstrap(verbose=False):
    printDebug('The following ontologies will be imported:')
    printDebug('--------------')
    count = 0
    for s in BOOTSTRAP_ONTOLOGIES:
        count += 1
        print(count, '<%s>' % s)
    printDebug('--------------')
    printDebug('Note: this operation may take several minutes.')
    printDebug('Proceed? [Y/N]')
    var = input()
    if var == 'y' or var == 'Y':
        for uri in BOOTSTRAP_ONTOLOGIES:
            try:
                printDebug('--------------')
                action_import(uri, verbose)
            except:
                printDebug(
                    'OPS... An Unknown Error Occurred - Aborting Installation')
        printDebug('\n==========\n' + 'Bootstrap command completed.',
            'important')
        return True
    else:
        printDebug('--------------')
        printDebug('Goodbye')
        return False