def create_albaran_automatic(pk, list_lines):
    line_bd = SalesLineAlbaran.objects.filter(line_order__pk__in=list_lines
        ).values_list('line_order__pk')
    if line_bd.count() == 0 or len(list_lines) != len(line_bd[0]):
        if line_bd.count() != 0:
            for x in line_bd[0]:
                list_lines.pop(list_lines.index(x))
        GenLineProduct.create_albaran_from_order(pk, list_lines)