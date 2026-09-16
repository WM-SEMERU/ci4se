def rec2latex(r, filename, empty=''):
    with open(filename, 'w') as latex:
        latex.write(s_rec2latex(r, empty=empty))
    return filename