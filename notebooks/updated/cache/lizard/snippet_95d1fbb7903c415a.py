def removeModifications(peptide):
    while peptide.find('[') != -1:
        peptide = peptide.split('[', 1)[0] + peptide.split(']', 1)[1]
    return peptide