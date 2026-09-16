def _print_summary(case, summary):
    for dof, data in summary.items():
        b4b = data['Bit for Bit']
        conf = data['Configurations']
        stdout = data['Std. Out Files']
        print('    ' + case + ' ' + str(dof))
        print('    --------------------')
        print('     Bit for bit matches   : ' + str(b4b[0]) + ' of ' + str(
            b4b[1]))
        print('     Configuration matches : ' + str(conf[0]) + ' of ' + str
            (conf[1]))
        print('     Std. Out files parsed : ' + str(stdout))
        print('')