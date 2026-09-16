def load_ns_sequence(eos_name):
    ns_sequence = []
    if eos_name == '2H':
        ns_sequence_path = os.path.join(pycbc.tmpltbank.
            NS_SEQUENCE_FILE_DIRECTORY, 'equil_2H.dat')
        ns_sequence = np.loadtxt(ns_sequence_path)
    else:
        print('Only the 2H EOS is currently supported!')
        print('If you plan to use a different NS EOS, be sure not to filter')
        print('too many templates!\n')
        raise Exception('Unsupported EOS!')
    max_ns_g_mass = max(ns_sequence[:, (0)])
    return ns_sequence, max_ns_g_mass