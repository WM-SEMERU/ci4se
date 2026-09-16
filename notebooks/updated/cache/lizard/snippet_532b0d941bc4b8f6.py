def match(self, other):
    colortext.message('FASTA Match')
    for frompdbID, fromchains in sorted(self.iteritems()):
        matched_pdbs = {}
        matched_chains = {}
        for fromchain, fromsequence in fromchains.iteritems():
            for topdbID, tochains in other.iteritems():
                for tochain, tosequence in tochains.iteritems():
                    if fromsequence == tosequence:
                        matched_pdbs[topdbID] = matched_pdbs.get(topdbID, set()
                            )
                        matched_pdbs[topdbID].add(fromchain)
                        matched_chains[fromchain] = matched_chains.get(
                            fromchain, [])
                        matched_chains[fromchain].append((topdbID, tochain))
        foundmatches = []
        colortext.printf('  %s' % frompdbID, color='silver')
        for mpdbID, mchains in matched_pdbs.iteritems():
            if mchains == set(fromchains.keys()):
                foundmatches.append(mpdbID)
                colortext.printf('  PDB %s matched PDB %s on all chains' %
                    (mpdbID, frompdbID), color='white')
        if foundmatches:
            for fromchain, fromsequence in fromchains.iteritems():
                colortext.printf('    %s' % fromchain, color='silver')
                colortext.printf('      %s' % fromsequence, color=self.
                    unique_sequences[fromsequence])
                mstr = []
                for mchain in matched_chains[fromchain]:
                    if mchain[0] in foundmatches:
                        mstr.append('%s chain %s' % (mchain[0], mchain[1]))
                colortext.printf('\t  Matches: %s' % ', '.join(mstr))
        else:
            colortext.error('    No matches found.')