def minimal_raw_seqs(self):
    seqs = [[], []]
    for letter in self.oneletter:
        if one2two.has_key(letter):
            seqs[0].append(one2two[letter][0])
            seqs[1].append(one2two[letter][1])
        else:
            seqs[0].append(letter)
            seqs[1].append(letter)
    if ''.join(seqs[0]) == ''.join(seqs[1]):
        return [''.join(seqs[0])]
    else:
        return [''.join(seqs[0]), ''.join(seqs[0])]