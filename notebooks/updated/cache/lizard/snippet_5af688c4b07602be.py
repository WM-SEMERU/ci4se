def sort(ctx):
    head = ctx.parent.head
    vcf_handle = ctx.parent.handle
    outfile = ctx.parent.outfile
    silent = ctx.parent.silent
    print_headers(head, outfile=outfile, silent=silent)
    for line in sort_variants(vcf_handle):
        print_variant(variant_line=line, outfile=outfile, silent=silent)