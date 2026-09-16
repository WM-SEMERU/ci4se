def is_fasta(filename):
    if re.search('\\.fa*s[ta]*$', filename, flags=re.I):
        return True
    elif re.search('\\.fa$', filename, flags=re.I):
        return True
    else:
        return False