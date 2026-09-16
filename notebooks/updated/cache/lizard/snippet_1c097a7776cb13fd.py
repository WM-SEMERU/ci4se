def create_invoice_from_albaran(pk, list_lines):
    context = {}
    if list_lines:
        new_list_lines = [x[0] for x in SalesLineAlbaran.objects.
            values_list('line_order__pk').filter(pk__in=[int(x) for x in
            list_lines]).exclude(invoiced=True)]
        if new_list_lines:
            lo = SalesLineOrder.objects.values_list('order__pk').filter(pk__in
                =new_list_lines)[:1]
            if lo and lo[0] and lo[0][0]:
                new_pk = lo[0][0]
                context = GenLineProduct.create_invoice_from_order(new_pk,
                    new_list_lines)
                if 'error' not in context or not context['error']:
                    SalesLineAlbaran.objects.filter(pk__in=[int(x) for x in
                        list_lines]).exclude(invoiced=True).update(invoiced
                        =True)
                return context
            else:
                error = _('Pedido no encontrado')
        else:
            error = _('Lineas no relacionadas con pedido')
    else:
        error = _('Lineas no seleccionadas')
    context['error'] = error
    return context