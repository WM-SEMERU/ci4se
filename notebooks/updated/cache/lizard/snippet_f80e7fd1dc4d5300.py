def get_random(self, n, l=None):
    random_f = Fasta()
    if l:
        ids = self.ids[:]
        random.shuffle(ids)
        i = 0
        while i < n and len(ids) > 0:
            seq_id = ids.pop()
            if len(self[seq_id]) >= l:
                start = random.randint(0, len(self[seq_id]) - l)
                random_f['random%s' % (i + 1)] = self[seq_id][start:start + l]
                i += 1
        if len(random_f) != n:
            sys.stderr.write('Not enough sequences of required length')
            return
        else:
            return random_f
    else:
        choice = random.sample(self.ids, n)
        for i in range(n):
            random_f[choice[i]] = self[choice[i]]
    return random_f