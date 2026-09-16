def prt_gene_aart(self, geneids, prt=sys.stdout):
    patgene = self.datobj.kws['fmtgene']
    itemid2name = self.datobj.kws.get('itemid2name')
    prt.write('\n{HDR}\n'.format(HDR=self.str_hdr()))
    for geneid in geneids:
        symbol = '' if itemid2name is None else itemid2name.get(geneid, '')
        prt.write(patgene.format(AART=self.gene2aart[geneid], ID=geneid,
            NAME=symbol))