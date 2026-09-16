def get_arg_parse():
    objParser = argparse.ArgumentParser()
    objParser.add_argument('-strCsvPrf', required=True, metavar=
        '/path/to/my_prior_res', help=
        'Absolute file path of prior pRF results.                                  Ignored if in testing mode.'
        )
    objParser.add_argument('-strStmApr', required=True, metavar=
        '/path/to/my_prior_res', help=
        'Absolute file path to npy file with                                  stimulus apertures. Ignored if in testing                                  mode.'
        )
    objParser.add_argument('-lgcNoise', dest='lgcNoise', action=
        'store_true', default=False, help=
        'Should noise be added to the simulated pRF                                 time course?'
        )
    objParser.add_argument('-lgcRtnNrl', dest='lgcRtnNrl', action=
        'store_true', default=False, help=
        'Should neural time course, unconvolved with                                  hrf, be returned as well?'
        )
    objParser.add_argument('-supsur', nargs='+', help=
        'List of floats that represent the ratio of                                  size neg surround to size pos center.'
        , type=float, default=None)
    objNspc = objParser.parse_args()
    return objNspc