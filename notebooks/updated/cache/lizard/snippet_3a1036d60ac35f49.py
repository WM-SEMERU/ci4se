def _fetch_seq(self):
    exons = []
    three_prime_ss = []
    five_prime_ss = []
    num_exons = self.bed.get_num_exons()
    for i in range(num_exons):
        tmp_id = '{0};exon{1}'.format(self.bed.gene_name, i)
        tmp_exon = self.fasta.fetch(reference=tmp_id)
        exons.append(tmp_exon)
        tmp_id_3ss = '{0};3SS'.format(tmp_id)
        tmp_id_5ss = '{0};5SS'.format(tmp_id)
        if num_exons == 1:
            pass
        elif i == 0:
            tmp_5ss = self.fasta.fetch(tmp_id_5ss)
            five_prime_ss.append(tmp_5ss)
        elif i == num_exons - 1:
            tmp_3ss = self.fasta.fetch(tmp_id_3ss)
            three_prime_ss.append(tmp_3ss)
        else:
            tmp_3ss = self.fasta.fetch(tmp_id_3ss)
            tmp_5ss = self.fasta.fetch(tmp_id_5ss)
            three_prime_ss.append(tmp_3ss)
            five_prime_ss.append(tmp_5ss)
    return exons, five_prime_ss, three_prime_ss