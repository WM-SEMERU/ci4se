def gene_panel(self, ax, feature):
    from gffutils.contrib.plotting import Gene
    extent = [feature.start, feature.stop]
    nearby_genes = self.db.region((feature.chrom, feature.start, feature.
        stop), featuretype='gene')
    ybase = 0
    ngenes = 0
    for nearby_gene in nearby_genes:
        ngenes += 1
        extent.extend([nearby_gene.start, nearby_gene.stop])
        gene_collection = Gene(self.db, nearby_gene, transcripts=['mRNA'],
            cds=['CDS'], utrs=['exon'], ybase=ybase, color='0.5', picker=5)
        gene_collection.name = nearby_gene.id
        gene_collection.add_to_ax(ax)
        ybase += gene_collection.max_y
    xmin = min(extent)
    xmax = max(extent)
    ymax = ngenes
    padding = (xmax - xmin) * 0.01
    ax.axis('tight')
    vline_kwargs = dict(color='k', linestyle='--')
    ax.axvline(feature.start, **vline_kwargs)
    ax.axvline(feature.stop, **vline_kwargs)
    interval = pybedtools.create_interval_from_list(feature.fields)
    interval.start = xmin - padding
    interval.stop = xmax + padding
    interval.strand = '.'
    return interval